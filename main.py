#!/usr/bin/env python3
import base64
import contextlib
import logging
import sys
import signal
import threading
import argparse
import multiprocessing

import grpc
import yaml

import psdbconnect.v1alpha1_pb2
import psdbconnect.v1alpha1_pb2_grpc
import vitess.query_pb2

_AUTHORIZATION_HEADER_KEY = "authorization"
LAST_CURSOR: psdbconnect.v1alpha1_pb2.TableCursor = None


class BasicAuthMetadataPlugin(grpc.AuthMetadataPlugin):

    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password = password

    def __call__(self, context: grpc.AuthMetadataContext, callback: grpc.AuthMetadataPluginCallback):
        """Implements authentication by passing metadata to a callback.

        Implementations of this method must not block.

        Args:
          context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
          callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        """
        callback(((_AUTHORIZATION_HEADER_KEY, self.get_authorization_token()),), None)

    def get_authorization_token(self):
        base64_str = base64.b64encode((self.username + ":" + self.password).encode('ascii')).decode('ascii')
        return "Basic " + base64_str


@contextlib.contextmanager
def create_client_channel(address: str, username: str, password: str, port: int = 443):
    ssl_config = grpc.ssl_channel_credentials()
    auth_config = grpc.metadata_call_credentials(BasicAuthMetadataPlugin(username, password))

    credentials = grpc.composite_channel_credentials(
        ssl_config,
        auth_config
    )
    channel = grpc.secure_channel(f"{address}:{port}", credentials)
    yield channel


def send_rpc(channel: grpc.Channel, request: psdbconnect.v1alpha1_pb2.SyncRequest, loglevel: int = logging.INFO) \
        -> psdbconnect.v1alpha1_pb2.TableCursor:
    stub = psdbconnect.v1alpha1_pb2_grpc.ConnectStub(channel)

    try:
        responses = stub.Sync(request)
    except grpc.RpcError as rpc_error:
        logging.error("Received error: %s", rpc_error)
        return rpc_error
    else:
        try:
            for response in responses:
                try:
                    logging.debug("Received message: %s", response)
                    threading.Thread(target=process_inserts, args=(response, loglevel, )).start()
                    threading.Thread(target=process_updates, args=(response, loglevel, )).start()
                    threading.Thread(target=process_deletes, args=(response, loglevel, )).start()

                except grpc.RpcError as rpc_error:
                    logging.error("Received message: %s", rpc_error)
                    return response.cursor

            return response.cursor
        except Exception as e:
            status = e.code()
            details = e.details()
            debug = e.debug_error_string()
            logging.error(f"status: {status}, details: {details}")
            logging.debug(debug)
            return LAST_CURSOR


def process_cursor(cursor: psdbconnect.v1alpha1_pb2.TableCursor):
    global LAST_CURSOR
    LAST_CURSOR = cursor
    logging.debug(f"cursor: shard={cursor.shard}, keyspace={cursor.keyspace}, position={cursor.position}")


def process_inserts(response: psdbconnect.v1alpha1_pb2.SyncResponse, loglevel: int = logging.INFO):
    logging.basicConfig(level=loglevel)
    for result in response.result:
        output = print_row(result)
        print("inserted row: " + ", ".join(output))
        process_cursor(response.cursor)


def process_updates(response: psdbconnect.v1alpha1_pb2.SyncResponse, loglevel: int = logging.INFO):
    logging.basicConfig(level=loglevel)
    for result in response.updates:
        output = print_row(result.before)
        print("updated before row: " + ", ".join(output))
        output = print_row(result.after)
        print("updated after row: " + ", ".join(output))
        process_cursor(response.cursor)


def process_deletes(response: psdbconnect.v1alpha1_pb2.SyncResponse, loglevel: int = logging.INFO):
    logging.basicConfig(level=loglevel)
    for result in response.deletes:
        output = print_row(result.result)
        print("deleted row: " + ", ".join(output))
        process_cursor(response.cursor)


def print_row(result: vitess.query_pb2.QueryResult):
    output = []
    i = 0
    for field in result.fields:
        if i == 0:
            output.append(f"`{field.database}`.`{field.table}`")
        for row in result.rows:
            output.append(f"{field.name} = {get_row_value(row, i)}")
            i += 1
    return output


def get_row_value(row: vitess.query_pb2.Row, field_num: int):
    if field_num == 0:
        return row.values[0:row.lengths[0]]
    else:
        start = 0
        for i in range(0, field_num):
            start += row.lengths[i]
        end = start + row.lengths[field_num]
        return row.values[start:end]


def run(connection, username: str, password: str, keyspace: str, table_name: str, columns=[], settings=[],
        shard: str = "", last_position: str = "", loglevel: int = logging.INFO):
    cursor = psdbconnect.v1alpha1_pb2.TableCursor(
        keyspace=keyspace,
        shard=shard,
        position=last_position
    )
    logging.basicConfig(level=loglevel)

    request = psdbconnect.v1alpha1_pb2.SyncRequest(
        table_name=table_name,
        columns=columns,
        tablet_type=psdbconnect.v1alpha1_pb2.TabletType.replica,
        cursor=cursor,
        include_inserts=settings['include_inserts'],
        include_updates=settings['include_updates'],
        include_deletes=settings['include_deletes'],
    )

    with create_client_channel(connection['hostname'], username, password, connection['port']) as channel:
        last_cursor = send_rpc(channel, request, loglevel)
        process_cursor(last_cursor)


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!, stopping.')
    for process in processes:
        process.terminate()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    parser = argparse.ArgumentParser(
        prog="./main.py",
        description="Example program for connecting to a PlanetScale Database using PlanetScale Connect.",
        epilog="This is just an example, no guarantees are provided",
    )

    parser.add_argument("-f", "--config", default="config.yml", dest="config")
    parser.add_argument("-l", "--log-level",
                        default="info",
                        choices=["info", "warning", "error", "debug"],
                        dest="loglevel"
                        )
    parser.add_argument("shard", nargs="?", help="(optional) the shard you want to query")
    parser.add_argument("position", nargs="?", help="(optional) the GTID position to start streaming from "
                                                    "(if you apecify this you need to specify the shard that "
                                                    "corresponds with this GTID)")
    args = parser.parse_args()
    # print(args)

    if args.loglevel == "info":
        logging.basicConfig(level=logging.INFO)
    elif args.loglevel == "warning":
        logging.basicConfig(level=logging.WARNING)
    elif args.loglevel == "error":
        logging.basicConfig(level=logging.ERROR)
    elif args.loglevel == "debug":
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)
        # print(config)

        if not config['credentials']:
            print("Error: no credentials specified")
            exit(-1)

        if not config['tables']:
            print("Error: no tables specified")
            exit(-1)

        if not config['credentials']['username'] \
                or not config['credentials']['username']:
            print("Error: username or password not specified")
            exit(-1)

        if not config['connection']:
            config['connection'] = {
                'hostname': 'aws.connect.psdb.cloud',
                'port': 443,
            }

        if not config['connection']['hostname']:
            config['connection']['hostname'] = 'aws.connect.psdb.cloud'

        if not config['connection']['port']:
            config['connection']['port'] = 443

        if not config['connection']['keyspace']:
            print("Error: keyspace not specified")
            exit(-1)

        if not config['settings']:
            config['settings'] = {
                'include_inserts': True,
                'include_updates': True,
                'include_deletes': True,
            }

        if not config['settings']['include_inserts']:
            config['settings']['include_inserts'] = True

        if not config['settings']['include_updates']:
            config['settings']['include_updates'] = True

        if not config['settings']['include_deletes']:
            config['settings']['include_deletes'] = True

        if not config['tables']:
            print("Error: no tables specified")
            exit(-1)

        processes = list()
        logging.info("Starting...")
        for table in config['tables']:
            logging.info(f"Starting for table {table['name']}")
            proc = multiprocessing.Process(target=run, args=(
                config['connection'],
                config['credentials']['username'],
                config['credentials']['password'],
                config['connection']['keyspace'],
                table['name'],
                table['columns'] if hasattr(table, 'column') else [],
                config['settings'],
                args.shard,
                args.position,
                logging.getLogger().getEffectiveLevel()
            ))
            proc.start()
            processes.append(proc)

        for proc in processes:
            proc.join()

        logging.info("All done!")
