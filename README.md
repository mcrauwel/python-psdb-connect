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

## Example output
```bash
(venv) ➜  python-psdb-connect git:(main) ✗ ./main.py $PSDB_USER $PSDB_PASS mcrauwel-test
row: id = b'1', k = b'49867', c = b'31451373586-15688153734-79729593694-96509299839-83724898275-86711833539-78981337422-35049690573-51724173961-87474696253'
row: id = b'2', k = b'49778', c = b'21472970079-70972780322-70018558993-71769650003-09270326047-32417012031-10768856803-14235120402-93989080412-18690312264'
row: id = b'3', k = b'49896', c = b'49376827441-24903985029-56844662308-79012577859-40518387141-60588419212-24399130405-42612257832-29494881732-71506024440'
row: id = b'4', k = b'51873', c = b'85762858421-36258200885-10758669419-44272723583-12529521893-95630803635-53907705724-07005352902-43001596772-53048338959'
row: id = b'5', k = b'50249', c = b'24805466175-85245528617-94635882649-46305216925-28637832581-03224489581-68883711727-95491561683-91969681472-12022277774'
row: id = b'6', k = b'50078', c = b'52892836230-54177743992-01821871718-48412537487-30066596248-87215430797-00375777469-64498831720-58542556455-90784765418'
row: id = b'7', k = b'50147', c = b'85820931248-14475640036-11980694501-86588543167-31029306229-09626867980-90685354565-02350460358-25863585366-53793794448'
row: id = b'8', k = b'49784', c = b'81578049255-33453976301-67096870761-27658738403-30546242249-53677469854-26594573136-34292002037-52736825353-99165193170'
row: id = b'9', k = b'49960', c = b'02844262904-89815504820-46476698406-25828746135-14201395324-78201250152-94654394113-77666987600-97276171313-77528982779'
```