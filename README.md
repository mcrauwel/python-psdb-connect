# Python PlanetScale connect example

This tool serves as an example on how to connect with [PlanetScale Connect](https://planetscale.com/docs/concepts/planetscale-connect) for ETL workflows.
This is merely an example and does not come with any guarantees whatsoever.

The protobuf files used in this example can be found [here](https://buf.build/planetscale)

## How you use it

This tool requires Python 3 to run.

Dependencies:
- grpcio
- grpcio-tools (only to regenerate the protobuf files)

Execution:

```bash
Usage: ./main.py <username> <password> <keyspace> [shard] [position]
```

Parameters:
- `username/password` to be generated in the [PlanetScale app](https://app.planetscale.com) (Note: you will need an "Edge" password to use this tool)
- `keyspace` the name of the keyspace you want to query
- `shard` (optional), the shard you want to query
- `position` (optional), the GTID position to start streaming from (if you specify this you need to specify the shard that corresponds with this GTID)

## Generating protobuf files

```bash
python -m grpc_tools.protoc --fatal_warnings  -Iproto -Iproto/vitess -Iproto/google/protobuf --python_out=. --grpc_python_out=. --pyi_out=. proto/google/protobuf/*.proto
python -m grpc_tools.protoc --fatal_warnings  -Iproto -Iproto/vitess -Iproto/google/protobuf --python_out=. --grpc_python_out=. --pyi_out=. proto/vitess/*.proto 
python -m grpc_tools.protoc --fatal_warnings  -Iproto -Iproto/vitess -Iproto/google/protobuf --python_out=. --grpc_python_out=. --pyi_out=. proto/psdbconnect/*.proto  
```