#!/usr/bin/env python3
import base64
import contextlib
import logging
import sys
import signal
import _thread

import grpc

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


def send_rpc(channel: grpc.Channel, request: psdbconnect.v1alpha1_pb2.SyncRequest) -> psdbconnect.v1alpha1_pb2.TableCursor:
    stub = psdbconnect.v1alpha1_pb2_grpc.ConnectStub(channel)

    try:
        responses = stub.Sync(request)
    except grpc.RpcError as rpc_error:
        logging.error("Received error: %s", rpc_error)
        return rpc_error
    else:
        for response in responses:
            try:
                logging.debug("Received message: %s", response)
                _thread.start_new_thread(process_inserts, (response, ))
                _thread.start_new_thread(process_updates, (response, ))
                _thread.start_new_thread(process_deletes, (response, ))

            except grpc.RpcError as rpc_error:
                logging.error("Received message: %s", rpc_error)
                return response.cursor

        return response.cursor


def process_cursor(cursor: psdbconnect.v1alpha1_pb2.TableCursor):
    global LAST_CURSOR
    LAST_CURSOR = cursor
    print(f"cursor: shard={cursor.shard}, keyspace={cursor.keyspace}, position={cursor.position}, lastKnownPK={cursor.last_known_pk}")


def process_inserts(response: psdbconnect.v1alpha1_pb2.SyncResponse):
    for result in response.result:
        output = print_row(result)
        print("inserted row: " + ", ".join(output))
        process_cursor(response.cursor)


def process_updates(response: psdbconnect.v1alpha1_pb2.SyncResponse):
    for result in response.updates:
        output = print_row(result.before)
        print("updated before row: " + ", ".join(output))
        output = print_row(result.after)
        print("updated after row: " + ", ".join(output))
        process_cursor(response.cursor)


def process_deletes(response: psdbconnect.v1alpha1_pb2.SyncResponse):
    for result in response.deletes:
        output = print_row(result.result)
        print("deleted row: " + ", ".join(output))
        process_cursor(response.cursor)


def print_row(result: vitess.query_pb2.QueryResult):
    output = []
    i = 0
    for field in result.fields:
        for row in result.rows:
            output.append(f"{field.name} = {get_row_value(row, i)}")
            i += 1
    return output


def get_row_value(row: vitess.query_pb2.Row, field_num: int):
    if field_num == 0:
        return row.values[0:row.lengths[0]]
    else:
        start = 0
        end = 0
        for i in range(0, field_num):
            start += row.lengths[i]
            end += start + row.lengths[i+1]
        return row.values[start:end]


def run(username: str, password: str, keyspace: str, shard: str = "", last_position: str = ""):
    cursor = psdbconnect.v1alpha1_pb2.TableCursor(
        keyspace=keyspace,
        shard=shard,
        position=last_position
    )
    request = psdbconnect.v1alpha1_pb2.SyncRequest(
        table_name="sbtest1",
        columns=["id", "k", "c"],
        tablet_type=psdbconnect.v1alpha1_pb2.TabletType.replica,
        cursor=cursor,
        include_inserts=True,
        include_updates=True,
        include_deletes=True,
    )

    with create_client_channel("aws.connect.psdb.cloud", username, password) as channel:
        last_cursor = send_rpc(channel, request)
        process_cursor(last_cursor)


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!, stopping. Here is your final cursor:')
    process_cursor(LAST_CURSOR)
    sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    signal.signal(signal.SIGINT, signal_handler)

    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <keyspace> [shard] [position]")
        exit(-1)

    if len(sys.argv) == 4:
        run(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

