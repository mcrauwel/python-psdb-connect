# Python PlanetScale connect example

This tool serves as an example on how to connect with [PlanetScale Connect](https://planetscale.com/docs/concepts/planetscale-connect) for ETL workflows.
This is merely an example and does not come with any guarantees whatsoever.

The protobuf files used in this example can be found [here](https://buf.build/planetscale)

## How you use it

This tool requires Python 3 to run.

Dependencies:
- grpcio
- grpcio-tools (only to regenerate the protobuf files)
- pyyaml

Execution:

```bash
usage: ./main.py [-h] [-f CONFIG] [-l {info,warning,error,debug}] [shard] [position]

Example program for connecting to a PlanetScale Database using PlanetScale Connect.

positional arguments:
  shard                 (optional) the shard you want to query
  position              (optional) the GTID position to start streaming from (if you apecify this you need to specify the shard that corresponds with this GTID)
  
optional arguments:
  -h, --help            show this help message and exit
  -f CONFIG, --config CONFIG
  -l {info,warning,error,debug}, --log-level {info,warning,error,debug}

This is just an example, no guarantees are provided
```

Config file spec:
```yaml
---
credentials:
  username: ""                       # required
  password: ""                       # required

connection:
  hostname: "aws.connect.psdb.cloud" # optional, will default to "aws.connect.psdb.cloud"
  port: 443                          # optional, will default to 443
  keyspace: ""                       # required

tables:                              # at least one table is required
  - name: "sbtest1"                  # required
    columns: ["id"]                  # optional, will default to empty list, meaning all columns

settings:
  include_inserts: true              # do you want the inserts>
  include_updates: true              # do you want the updates?
  include_deletes: true              # do you want the deletes?
```

## Generating protobuf files

```bash
python -m grpc_tools.protoc --fatal_warnings  -Iproto -Iproto/vitess -Iproto/google/protobuf --python_out=. --grpc_python_out=. --pyi_out=. proto/google/protobuf/*.proto
python -m grpc_tools.protoc --fatal_warnings  -Iproto -Iproto/vitess -Iproto/google/protobuf --python_out=. --grpc_python_out=. --pyi_out=. proto/vitess/*.proto 
python -m grpc_tools.protoc --fatal_warnings  -Iproto -Iproto/vitess -Iproto/google/protobuf --python_out=. --grpc_python_out=. --pyi_out=. proto/psdbconnect/*.proto  
```

## Example output
```bash
(venv) ➜  python-psdb-connect git:(main) ✗ ./main.py -f config.yml
INFO:root:Starting...
INFO:root:Starting for table sbtest1
inserted row: `example`.`sbtest1` , id = b'1', k = b'1', c = b'test'
inserted row: `example`.`sbtest1` , id = b'2', k = b'4', c = b'test'
inserted row: `example`.`sbtest1` , id = b'3', k = b'3', c = b'test'
inserted row: `example`.`sbtest1` , id = b'4', k = b'4', c = b'test'
inserted row: `example`.`sbtest1` , id = b'5', k = b'5', c = b'test'
inserted row: `example`.`sbtest1` , id = b'6', k = b'1', c = b'test'
inserted row: `example`.`sbtest1` , id = b'7', k = b'2', c = b'test'
inserted row: `example`.`sbtest1` , id = b'8', k = b'3', c = b'test'
inserted row: `example`.`sbtest1` , id = b'9', k = b'4', c = b'test'
```