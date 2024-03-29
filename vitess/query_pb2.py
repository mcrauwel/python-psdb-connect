# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vitess/query.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vitess import topodata_pb2 as vitess_dot_topodata__pb2
from vitess import vtrpc_pb2 as vitess_dot_vtrpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12vitess/query.proto\x12\x05query\x1a\x15vitess/topodata.proto\x1a\x12vitess/vtrpc.proto\"b\n\x06Target\x12\x10\n\x08keyspace\x18\x01 \x01(\t\x12\r\n\x05shard\x18\x02 \x01(\t\x12)\n\x0btablet_type\x18\x03 \x01(\x0e\x32\x14.topodata.TabletType\x12\x0c\n\x04\x63\x65ll\x18\x04 \x01(\t\"2\n\x0eVTGateCallerID\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06groups\x18\x02 \x03(\t\"@\n\nEventToken\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\r\n\x05shard\x18\x02 \x01(\t\x12\x10\n\x08position\x18\x03 \x01(\t\"1\n\x05Value\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.query.Type\x12\r\n\x05value\x18\x02 \x01(\x0c\"V\n\x0c\x42indVariable\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.query.Type\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1c\n\x06values\x18\x03 \x03(\x0b\x32\x0c.query.Value\"\xa2\x01\n\nBoundQuery\x12\x0b\n\x03sql\x18\x01 \x01(\t\x12<\n\x0e\x62ind_variables\x18\x02 \x03(\x0b\x32$.query.BoundQuery.BindVariablesEntry\x1aI\n\x12\x42indVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.query.BindVariable:\x02\x38\x01\"\xba\x06\n\x0e\x45xecuteOptions\x12=\n\x0fincluded_fields\x18\x04 \x01(\x0e\x32$.query.ExecuteOptions.IncludedFields\x12\x19\n\x11\x63lient_found_rows\x18\x05 \x01(\x08\x12\x30\n\x08workload\x18\x06 \x01(\x0e\x32\x1e.query.ExecuteOptions.Workload\x12\x18\n\x10sql_select_limit\x18\x08 \x01(\x03\x12I\n\x15transaction_isolation\x18\t \x01(\x0e\x32*.query.ExecuteOptions.TransactionIsolation\x12\x1d\n\x15skip_query_plan_cache\x18\n \x01(\x08\x12=\n\x0fplanner_version\x18\x0b \x01(\x0e\x32$.query.ExecuteOptions.PlannerVersion\x12\x1f\n\x17has_created_temp_tables\x18\x0c \x01(\x08\";\n\x0eIncludedFields\x12\x11\n\rTYPE_AND_NAME\x10\x00\x12\r\n\tTYPE_ONLY\x10\x01\x12\x07\n\x03\x41LL\x10\x02\"8\n\x08Workload\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04OLTP\x10\x01\x12\x08\n\x04OLAP\x10\x02\x12\x07\n\x03\x44\x42\x41\x10\x03\"\xa7\x01\n\x14TransactionIsolation\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x13\n\x0fREPEATABLE_READ\x10\x01\x12\x12\n\x0eREAD_COMMITTED\x10\x02\x12\x14\n\x10READ_UNCOMMITTED\x10\x03\x12\x10\n\x0cSERIALIZABLE\x10\x04\x12!\n\x1d\x43ONSISTENT_SNAPSHOT_READ_ONLY\x10\x05\x12\x0e\n\nAUTOCOMMIT\x10\x06\"\x84\x01\n\x0ePlannerVersion\x12\x13\n\x0f\x44\x45\x46\x41ULT_PLANNER\x10\x00\x12\x06\n\x02V3\x10\x01\x12\x08\n\x04Gen4\x10\x02\x12\x0e\n\nGen4Greedy\x10\x03\x12\x12\n\x0eGen4Left2Right\x10\x04\x12\x14\n\x10Gen4WithFallback\x10\x05\x12\x11\n\rGen4CompareV3\x10\x06J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"\xd4\x01\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.query.Type\x12\r\n\x05table\x18\x03 \x01(\t\x12\x11\n\torg_table\x18\x04 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x05 \x01(\t\x12\x10\n\x08org_name\x18\x06 \x01(\t\x12\x15\n\rcolumn_length\x18\x07 \x01(\r\x12\x0f\n\x07\x63harset\x18\x08 \x01(\r\x12\x10\n\x08\x64\x65\x63imals\x18\t \x01(\r\x12\r\n\x05\x66lags\x18\n \x01(\r\x12\x13\n\x0b\x63olumn_type\x18\x0b \x01(\t\"&\n\x03Row\x12\x0f\n\x07lengths\x18\x01 \x03(\x12\x12\x0e\n\x06values\x18\x02 \x01(\x0c\"u\n\x0bQueryResult\x12\x1c\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x0c.query.Field\x12\x15\n\rrows_affected\x18\x02 \x01(\x04\x12\x11\n\tinsert_id\x18\x03 \x01(\x04\x12\x18\n\x04rows\x18\x04 \x03(\x0b\x32\n.query.RowJ\x04\x08\x05\x10\x06\"-\n\x0cQueryWarning\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xca\x02\n\x0bStreamEvent\x12\x30\n\nstatements\x18\x01 \x03(\x0b\x32\x1c.query.StreamEvent.Statement\x12&\n\x0b\x65vent_token\x18\x02 \x01(\x0b\x32\x11.query.EventToken\x1a\xe0\x01\n\tStatement\x12\x37\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32%.query.StreamEvent.Statement.Category\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12(\n\x12primary_key_fields\x18\x03 \x03(\x0b\x32\x0c.query.Field\x12&\n\x12primary_key_values\x18\x04 \x03(\x0b\x32\n.query.Row\x12\x0b\n\x03sql\x18\x05 \x01(\x0c\"\'\n\x08\x43\x61tegory\x12\t\n\x05\x45rror\x10\x00\x12\x07\n\x03\x44ML\x10\x01\x12\x07\n\x03\x44\x44L\x10\x02\"\x88\x02\n\x0e\x45xecuteRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12 \n\x05query\x18\x04 \x01(\x0b\x32\x11.query.BoundQuery\x12\x16\n\x0etransaction_id\x18\x05 \x01(\x03\x12&\n\x07options\x18\x06 \x01(\x0b\x32\x15.query.ExecuteOptions\x12\x13\n\x0breserved_id\x18\x07 \x01(\x03\"5\n\x0f\x45xecuteResponse\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\x12.query.QueryResult\"U\n\x0fResultWithError\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12\"\n\x06result\x18\x02 \x01(\x0b\x32\x12.query.QueryResult\"\x92\x02\n\x13\x45xecuteBatchRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\"\n\x07queries\x18\x04 \x03(\x0b\x32\x11.query.BoundQuery\x12\x16\n\x0e\x61s_transaction\x18\x05 \x01(\x08\x12\x16\n\x0etransaction_id\x18\x06 \x01(\x03\x12&\n\x07options\x18\x07 \x01(\x0b\x32\x15.query.ExecuteOptions\";\n\x14\x45xecuteBatchResponse\x12#\n\x07results\x18\x01 \x03(\x0b\x32\x12.query.QueryResult\"\xf9\x01\n\x14StreamExecuteRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12 \n\x05query\x18\x04 \x01(\x0b\x32\x11.query.BoundQuery\x12&\n\x07options\x18\x05 \x01(\x0b\x32\x15.query.ExecuteOptions\x12\x16\n\x0etransaction_id\x18\x06 \x01(\x03\";\n\x15StreamExecuteResponse\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\x12.query.QueryResult\"\xb7\x01\n\x0c\x42\x65ginRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12&\n\x07options\x18\x04 \x01(\x0b\x32\x15.query.ExecuteOptions\"T\n\rBeginResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x03\x12+\n\x0ctablet_alias\x18\x02 \x01(\x0b\x32\x15.topodata.TabletAlias\"\xa8\x01\n\rCommitRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\"%\n\x0e\x43ommitResponse\x12\x13\n\x0breserved_id\x18\x01 \x01(\x03\"\xaa\x01\n\x0fRollbackRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\"\'\n\x10RollbackResponse\x12\x13\n\x0breserved_id\x18\x01 \x01(\x03\"\xb7\x01\n\x0ePrepareRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\x12\x0c\n\x04\x64tid\x18\x05 \x01(\t\"\x11\n\x0fPrepareResponse\"\xa6\x01\n\x15\x43ommitPreparedRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x0c\n\x04\x64tid\x18\x04 \x01(\t\"\x18\n\x16\x43ommitPreparedResponse\"\xc0\x01\n\x17RollbackPreparedRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\x12\x0c\n\x04\x64tid\x18\x05 \x01(\t\"\x1a\n\x18RollbackPreparedResponse\"\xce\x01\n\x18\x43reateTransactionRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x0c\n\x04\x64tid\x18\x04 \x01(\t\x12#\n\x0cparticipants\x18\x05 \x03(\x0b\x32\r.query.Target\"\x1b\n\x19\x43reateTransactionResponse\"\xbb\x01\n\x12StartCommitRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\x12\x0c\n\x04\x64tid\x18\x05 \x01(\t\"\x15\n\x13StartCommitResponse\"\xbb\x01\n\x12SetRollbackRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\x12\x0c\n\x04\x64tid\x18\x05 \x01(\t\"\x15\n\x13SetRollbackResponse\"\xab\x01\n\x1a\x43oncludeTransactionRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x0c\n\x04\x64tid\x18\x04 \x01(\t\"\x1d\n\x1b\x43oncludeTransactionResponse\"\xa7\x01\n\x16ReadTransactionRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x0c\n\x04\x64tid\x18\x04 \x01(\t\"G\n\x17ReadTransactionResponse\x12,\n\x08metadata\x18\x01 \x01(\x0b\x32\x1a.query.TransactionMetadata\"\x8a\x02\n\x13\x42\x65ginExecuteRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12 \n\x05query\x18\x04 \x01(\x0b\x32\x11.query.BoundQuery\x12&\n\x07options\x18\x05 \x01(\x0b\x32\x15.query.ExecuteOptions\x12\x13\n\x0breserved_id\x18\x06 \x01(\x03\x12\x13\n\x0bpre_queries\x18\x07 \x03(\t\"\x9f\x01\n\x14\x42\x65ginExecuteResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12\"\n\x06result\x18\x02 \x01(\x0b\x32\x12.query.QueryResult\x12\x16\n\x0etransaction_id\x18\x03 \x01(\x03\x12+\n\x0ctablet_alias\x18\x04 \x01(\x0b\x32\x15.topodata.TabletAlias\"\xff\x01\n\x18\x42\x65ginExecuteBatchRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\"\n\x07queries\x18\x04 \x03(\x0b\x32\x11.query.BoundQuery\x12\x16\n\x0e\x61s_transaction\x18\x05 \x01(\x08\x12&\n\x07options\x18\x06 \x01(\x0b\x32\x15.query.ExecuteOptions\"\xa5\x01\n\x19\x42\x65ginExecuteBatchResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12#\n\x07results\x18\x02 \x03(\x0b\x32\x12.query.QueryResult\x12\x16\n\x0etransaction_id\x18\x03 \x01(\x03\x12+\n\x0ctablet_alias\x18\x04 \x01(\x0b\x32\x15.topodata.TabletAlias\"\xfb\x01\n\x19\x42\x65ginStreamExecuteRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12 \n\x05query\x18\x04 \x01(\x0b\x32\x11.query.BoundQuery\x12&\n\x07options\x18\x05 \x01(\x0b\x32\x15.query.ExecuteOptions\x12\x13\n\x0bpre_queries\x18\x06 \x03(\t\"\xa5\x01\n\x1a\x42\x65ginStreamExecuteResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12\"\n\x06result\x18\x02 \x01(\x0b\x32\x12.query.QueryResult\x12\x16\n\x0etransaction_id\x18\x03 \x01(\x03\x12+\n\x0ctablet_alias\x18\x04 \x01(\x0b\x32\x15.topodata.TabletAlias\"\xa5\x01\n\x14MessageStreamRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x0c\n\x04name\x18\x04 \x01(\t\";\n\x15MessageStreamResponse\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\x12.query.QueryResult\"\xbd\x01\n\x11MessageAckRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x19\n\x03ids\x18\x05 \x03(\x0b\x32\x0c.query.Value\"8\n\x12MessageAckResponse\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\x12.query.QueryResult\"\x8f\x02\n\x15ReserveExecuteRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12 \n\x05query\x18\x04 \x01(\x0b\x32\x11.query.BoundQuery\x12\x16\n\x0etransaction_id\x18\x05 \x01(\x03\x12&\n\x07options\x18\x06 \x01(\x0b\x32\x15.query.ExecuteOptions\x12\x13\n\x0bpre_queries\x18\x07 \x03(\t\"\x9e\x01\n\x16ReserveExecuteResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12\"\n\x06result\x18\x02 \x01(\x0b\x32\x12.query.QueryResult\x12\x13\n\x0breserved_id\x18\x03 \x01(\x03\x12+\n\x0ctablet_alias\x18\x04 \x01(\x0b\x32\x15.topodata.TabletAlias\"\x98\x02\n\x1aReserveBeginExecuteRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12 \n\x05query\x18\x04 \x01(\x0b\x32\x11.query.BoundQuery\x12&\n\x07options\x18\x05 \x01(\x0b\x32\x15.query.ExecuteOptions\x12\x13\n\x0bpre_queries\x18\x06 \x03(\t\x12\x1a\n\x12post_begin_queries\x18\x07 \x03(\t\"\xbb\x01\n\x1bReserveBeginExecuteResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12\"\n\x06result\x18\x02 \x01(\x0b\x32\x12.query.QueryResult\x12\x16\n\x0etransaction_id\x18\x03 \x01(\x03\x12\x13\n\x0breserved_id\x18\x04 \x01(\x03\x12+\n\x0ctablet_alias\x18\x05 \x01(\x0b\x32\x15.topodata.TabletAlias\"\xbe\x01\n\x0eReleaseRequest\x12,\n\x13\x65\x66\x66\x65\x63tive_caller_id\x18\x01 \x01(\x0b\x32\x0f.vtrpc.CallerID\x12\x32\n\x13immediate_caller_id\x18\x02 \x01(\x0b\x32\x15.query.VTGateCallerID\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.query.Target\x12\x16\n\x0etransaction_id\x18\x04 \x01(\x03\x12\x13\n\x0breserved_id\x18\x05 \x01(\x03\"\x11\n\x0fReleaseResponse\"\x15\n\x13StreamHealthRequest\"\xcc\x01\n\rRealtimeStats\x12\x14\n\x0chealth_error\x18\x01 \x01(\t\x12\x1f\n\x17replication_lag_seconds\x18\x02 \x01(\r\x12\x1c\n\x14\x62inlog_players_count\x18\x03 \x01(\x05\x12(\n filtered_replication_lag_seconds\x18\x04 \x01(\x03\x12\x11\n\tcpu_usage\x18\x05 \x01(\x01\x12\x0b\n\x03qps\x18\x06 \x01(\x01\x12\x1c\n\x14table_schema_changed\x18\x07 \x03(\t\"\x98\x01\n\x0e\x41ggregateStats\x12\x1c\n\x14healthy_tablet_count\x18\x01 \x01(\x05\x12\x1e\n\x16unhealthy_tablet_count\x18\x02 \x01(\x05\x12#\n\x1breplication_lag_seconds_min\x18\x03 \x01(\r\x12#\n\x1breplication_lag_seconds_max\x18\x04 \x01(\r\"\xd7\x01\n\x14StreamHealthResponse\x12\x1d\n\x06target\x18\x01 \x01(\x0b\x32\r.query.Target\x12\x0f\n\x07serving\x18\x02 \x01(\x08\x12.\n&tablet_externally_reparented_timestamp\x18\x03 \x01(\x03\x12,\n\x0erealtime_stats\x18\x04 \x01(\x0b\x32\x14.query.RealtimeStats\x12+\n\x0ctablet_alias\x18\x05 \x01(\x0b\x32\x15.topodata.TabletAliasJ\x04\x08\x06\x10\x07\"\x86\x01\n\x13TransactionMetadata\x12\x0c\n\x04\x64tid\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0e\x32\x17.query.TransactionState\x12\x14\n\x0ctime_created\x18\x03 \x01(\x03\x12#\n\x0cparticipants\x18\x04 \x03(\x0b\x32\r.query.Target*\x92\x03\n\tMySqlFlag\x12\t\n\x05\x45MPTY\x10\x00\x12\x11\n\rNOT_NULL_FLAG\x10\x01\x12\x10\n\x0cPRI_KEY_FLAG\x10\x02\x12\x13\n\x0fUNIQUE_KEY_FLAG\x10\x04\x12\x15\n\x11MULTIPLE_KEY_FLAG\x10\x08\x12\r\n\tBLOB_FLAG\x10\x10\x12\x11\n\rUNSIGNED_FLAG\x10 \x12\x11\n\rZEROFILL_FLAG\x10@\x12\x10\n\x0b\x42INARY_FLAG\x10\x80\x01\x12\x0e\n\tENUM_FLAG\x10\x80\x02\x12\x18\n\x13\x41UTO_INCREMENT_FLAG\x10\x80\x04\x12\x13\n\x0eTIMESTAMP_FLAG\x10\x80\x08\x12\r\n\x08SET_FLAG\x10\x80\x10\x12\x1a\n\x15NO_DEFAULT_VALUE_FLAG\x10\x80 \x12\x17\n\x12ON_UPDATE_NOW_FLAG\x10\x80@\x12\x0e\n\x08NUM_FLAG\x10\x80\x80\x02\x12\x13\n\rPART_KEY_FLAG\x10\x80\x80\x01\x12\x10\n\nGROUP_FLAG\x10\x80\x80\x02\x12\x11\n\x0bUNIQUE_FLAG\x10\x80\x80\x04\x12\x11\n\x0b\x42INCMP_FLAG\x10\x80\x80\x08\x1a\x02\x10\x01*k\n\x04\x46lag\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\nISINTEGRAL\x10\x80\x02\x12\x0f\n\nISUNSIGNED\x10\x80\x04\x12\x0c\n\x07ISFLOAT\x10\x80\x08\x12\r\n\x08ISQUOTED\x10\x80\x10\x12\x0b\n\x06ISTEXT\x10\x80 \x12\r\n\x08ISBINARY\x10\x80@*\xb3\x03\n\x04Type\x12\r\n\tNULL_TYPE\x10\x00\x12\t\n\x04INT8\x10\x81\x02\x12\n\n\x05UINT8\x10\x82\x06\x12\n\n\x05INT16\x10\x83\x02\x12\x0b\n\x06UINT16\x10\x84\x06\x12\n\n\x05INT24\x10\x85\x02\x12\x0b\n\x06UINT24\x10\x86\x06\x12\n\n\x05INT32\x10\x87\x02\x12\x0b\n\x06UINT32\x10\x88\x06\x12\n\n\x05INT64\x10\x89\x02\x12\x0b\n\x06UINT64\x10\x8a\x06\x12\x0c\n\x07\x46LOAT32\x10\x8b\x08\x12\x0c\n\x07\x46LOAT64\x10\x8c\x08\x12\x0e\n\tTIMESTAMP\x10\x8d\x10\x12\t\n\x04\x44\x41TE\x10\x8e\x10\x12\t\n\x04TIME\x10\x8f\x10\x12\r\n\x08\x44\x41TETIME\x10\x90\x10\x12\t\n\x04YEAR\x10\x91\x06\x12\x0b\n\x07\x44\x45\x43IMAL\x10\x12\x12\t\n\x04TEXT\x10\x93\x30\x12\t\n\x04\x42LOB\x10\x94P\x12\x0c\n\x07VARCHAR\x10\x95\x30\x12\x0e\n\tVARBINARY\x10\x96P\x12\t\n\x04\x43HAR\x10\x97\x30\x12\x0b\n\x06\x42INARY\x10\x98P\x12\x08\n\x03\x42IT\x10\x99\x10\x12\t\n\x04\x45NUM\x10\x9a\x10\x12\x08\n\x03SET\x10\x9b\x10\x12\t\n\x05TUPLE\x10\x1c\x12\r\n\x08GEOMETRY\x10\x9d\x10\x12\t\n\x04JSON\x10\x9e\x10\x12\x0e\n\nEXPRESSION\x10\x1f\x12\x0b\n\x06HEXNUM\x10\xa0 \x12\x0b\n\x06HEXVAL\x10\xa1 *F\n\x10TransactionState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PREPARE\x10\x01\x12\n\n\x06\x43OMMIT\x10\x02\x12\x0c\n\x08ROLLBACK\x10\x03\x42\x35\n\x0fio.vitess.protoZ\"vitess.io/vitess/go/vt/proto/queryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vitess.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017io.vitess.protoZ\"vitess.io/vitess/go/vt/proto/query'
  _globals['_MYSQLFLAG']._options = None
  _globals['_MYSQLFLAG']._serialized_options = b'\020\001'
  _globals['_BOUNDQUERY_BINDVARIABLESENTRY']._options = None
  _globals['_BOUNDQUERY_BINDVARIABLESENTRY']._serialized_options = b'8\001'
  _globals['_MYSQLFLAG']._serialized_start=9287
  _globals['_MYSQLFLAG']._serialized_end=9689
  _globals['_FLAG']._serialized_start=9691
  _globals['_FLAG']._serialized_end=9798
  _globals['_TYPE']._serialized_start=9801
  _globals['_TYPE']._serialized_end=10236
  _globals['_TRANSACTIONSTATE']._serialized_start=10238
  _globals['_TRANSACTIONSTATE']._serialized_end=10308
  _globals['_TARGET']._serialized_start=72
  _globals['_TARGET']._serialized_end=170
  _globals['_VTGATECALLERID']._serialized_start=172
  _globals['_VTGATECALLERID']._serialized_end=222
  _globals['_EVENTTOKEN']._serialized_start=224
  _globals['_EVENTTOKEN']._serialized_end=288
  _globals['_VALUE']._serialized_start=290
  _globals['_VALUE']._serialized_end=339
  _globals['_BINDVARIABLE']._serialized_start=341
  _globals['_BINDVARIABLE']._serialized_end=427
  _globals['_BOUNDQUERY']._serialized_start=430
  _globals['_BOUNDQUERY']._serialized_end=592
  _globals['_BOUNDQUERY_BINDVARIABLESENTRY']._serialized_start=519
  _globals['_BOUNDQUERY_BINDVARIABLESENTRY']._serialized_end=592
  _globals['_EXECUTEOPTIONS']._serialized_start=595
  _globals['_EXECUTEOPTIONS']._serialized_end=1421
  _globals['_EXECUTEOPTIONS_INCLUDEDFIELDS']._serialized_start=981
  _globals['_EXECUTEOPTIONS_INCLUDEDFIELDS']._serialized_end=1040
  _globals['_EXECUTEOPTIONS_WORKLOAD']._serialized_start=1042
  _globals['_EXECUTEOPTIONS_WORKLOAD']._serialized_end=1098
  _globals['_EXECUTEOPTIONS_TRANSACTIONISOLATION']._serialized_start=1101
  _globals['_EXECUTEOPTIONS_TRANSACTIONISOLATION']._serialized_end=1268
  _globals['_EXECUTEOPTIONS_PLANNERVERSION']._serialized_start=1271
  _globals['_EXECUTEOPTIONS_PLANNERVERSION']._serialized_end=1403
  _globals['_FIELD']._serialized_start=1424
  _globals['_FIELD']._serialized_end=1636
  _globals['_ROW']._serialized_start=1638
  _globals['_ROW']._serialized_end=1676
  _globals['_QUERYRESULT']._serialized_start=1678
  _globals['_QUERYRESULT']._serialized_end=1795
  _globals['_QUERYWARNING']._serialized_start=1797
  _globals['_QUERYWARNING']._serialized_end=1842
  _globals['_STREAMEVENT']._serialized_start=1845
  _globals['_STREAMEVENT']._serialized_end=2175
  _globals['_STREAMEVENT_STATEMENT']._serialized_start=1951
  _globals['_STREAMEVENT_STATEMENT']._serialized_end=2175
  _globals['_STREAMEVENT_STATEMENT_CATEGORY']._serialized_start=2136
  _globals['_STREAMEVENT_STATEMENT_CATEGORY']._serialized_end=2175
  _globals['_EXECUTEREQUEST']._serialized_start=2178
  _globals['_EXECUTEREQUEST']._serialized_end=2442
  _globals['_EXECUTERESPONSE']._serialized_start=2444
  _globals['_EXECUTERESPONSE']._serialized_end=2497
  _globals['_RESULTWITHERROR']._serialized_start=2499
  _globals['_RESULTWITHERROR']._serialized_end=2584
  _globals['_EXECUTEBATCHREQUEST']._serialized_start=2587
  _globals['_EXECUTEBATCHREQUEST']._serialized_end=2861
  _globals['_EXECUTEBATCHRESPONSE']._serialized_start=2863
  _globals['_EXECUTEBATCHRESPONSE']._serialized_end=2922
  _globals['_STREAMEXECUTEREQUEST']._serialized_start=2925
  _globals['_STREAMEXECUTEREQUEST']._serialized_end=3174
  _globals['_STREAMEXECUTERESPONSE']._serialized_start=3176
  _globals['_STREAMEXECUTERESPONSE']._serialized_end=3235
  _globals['_BEGINREQUEST']._serialized_start=3238
  _globals['_BEGINREQUEST']._serialized_end=3421
  _globals['_BEGINRESPONSE']._serialized_start=3423
  _globals['_BEGINRESPONSE']._serialized_end=3507
  _globals['_COMMITREQUEST']._serialized_start=3510
  _globals['_COMMITREQUEST']._serialized_end=3678
  _globals['_COMMITRESPONSE']._serialized_start=3680
  _globals['_COMMITRESPONSE']._serialized_end=3717
  _globals['_ROLLBACKREQUEST']._serialized_start=3720
  _globals['_ROLLBACKREQUEST']._serialized_end=3890
  _globals['_ROLLBACKRESPONSE']._serialized_start=3892
  _globals['_ROLLBACKRESPONSE']._serialized_end=3931
  _globals['_PREPAREREQUEST']._serialized_start=3934
  _globals['_PREPAREREQUEST']._serialized_end=4117
  _globals['_PREPARERESPONSE']._serialized_start=4119
  _globals['_PREPARERESPONSE']._serialized_end=4136
  _globals['_COMMITPREPAREDREQUEST']._serialized_start=4139
  _globals['_COMMITPREPAREDREQUEST']._serialized_end=4305
  _globals['_COMMITPREPAREDRESPONSE']._serialized_start=4307
  _globals['_COMMITPREPAREDRESPONSE']._serialized_end=4331
  _globals['_ROLLBACKPREPAREDREQUEST']._serialized_start=4334
  _globals['_ROLLBACKPREPAREDREQUEST']._serialized_end=4526
  _globals['_ROLLBACKPREPAREDRESPONSE']._serialized_start=4528
  _globals['_ROLLBACKPREPAREDRESPONSE']._serialized_end=4554
  _globals['_CREATETRANSACTIONREQUEST']._serialized_start=4557
  _globals['_CREATETRANSACTIONREQUEST']._serialized_end=4763
  _globals['_CREATETRANSACTIONRESPONSE']._serialized_start=4765
  _globals['_CREATETRANSACTIONRESPONSE']._serialized_end=4792
  _globals['_STARTCOMMITREQUEST']._serialized_start=4795
  _globals['_STARTCOMMITREQUEST']._serialized_end=4982
  _globals['_STARTCOMMITRESPONSE']._serialized_start=4984
  _globals['_STARTCOMMITRESPONSE']._serialized_end=5005
  _globals['_SETROLLBACKREQUEST']._serialized_start=5008
  _globals['_SETROLLBACKREQUEST']._serialized_end=5195
  _globals['_SETROLLBACKRESPONSE']._serialized_start=5197
  _globals['_SETROLLBACKRESPONSE']._serialized_end=5218
  _globals['_CONCLUDETRANSACTIONREQUEST']._serialized_start=5221
  _globals['_CONCLUDETRANSACTIONREQUEST']._serialized_end=5392
  _globals['_CONCLUDETRANSACTIONRESPONSE']._serialized_start=5394
  _globals['_CONCLUDETRANSACTIONRESPONSE']._serialized_end=5423
  _globals['_READTRANSACTIONREQUEST']._serialized_start=5426
  _globals['_READTRANSACTIONREQUEST']._serialized_end=5593
  _globals['_READTRANSACTIONRESPONSE']._serialized_start=5595
  _globals['_READTRANSACTIONRESPONSE']._serialized_end=5666
  _globals['_BEGINEXECUTEREQUEST']._serialized_start=5669
  _globals['_BEGINEXECUTEREQUEST']._serialized_end=5935
  _globals['_BEGINEXECUTERESPONSE']._serialized_start=5938
  _globals['_BEGINEXECUTERESPONSE']._serialized_end=6097
  _globals['_BEGINEXECUTEBATCHREQUEST']._serialized_start=6100
  _globals['_BEGINEXECUTEBATCHREQUEST']._serialized_end=6355
  _globals['_BEGINEXECUTEBATCHRESPONSE']._serialized_start=6358
  _globals['_BEGINEXECUTEBATCHRESPONSE']._serialized_end=6523
  _globals['_BEGINSTREAMEXECUTEREQUEST']._serialized_start=6526
  _globals['_BEGINSTREAMEXECUTEREQUEST']._serialized_end=6777
  _globals['_BEGINSTREAMEXECUTERESPONSE']._serialized_start=6780
  _globals['_BEGINSTREAMEXECUTERESPONSE']._serialized_end=6945
  _globals['_MESSAGESTREAMREQUEST']._serialized_start=6948
  _globals['_MESSAGESTREAMREQUEST']._serialized_end=7113
  _globals['_MESSAGESTREAMRESPONSE']._serialized_start=7115
  _globals['_MESSAGESTREAMRESPONSE']._serialized_end=7174
  _globals['_MESSAGEACKREQUEST']._serialized_start=7177
  _globals['_MESSAGEACKREQUEST']._serialized_end=7366
  _globals['_MESSAGEACKRESPONSE']._serialized_start=7368
  _globals['_MESSAGEACKRESPONSE']._serialized_end=7424
  _globals['_RESERVEEXECUTEREQUEST']._serialized_start=7427
  _globals['_RESERVEEXECUTEREQUEST']._serialized_end=7698
  _globals['_RESERVEEXECUTERESPONSE']._serialized_start=7701
  _globals['_RESERVEEXECUTERESPONSE']._serialized_end=7859
  _globals['_RESERVEBEGINEXECUTEREQUEST']._serialized_start=7862
  _globals['_RESERVEBEGINEXECUTEREQUEST']._serialized_end=8142
  _globals['_RESERVEBEGINEXECUTERESPONSE']._serialized_start=8145
  _globals['_RESERVEBEGINEXECUTERESPONSE']._serialized_end=8332
  _globals['_RELEASEREQUEST']._serialized_start=8335
  _globals['_RELEASEREQUEST']._serialized_end=8525
  _globals['_RELEASERESPONSE']._serialized_start=8527
  _globals['_RELEASERESPONSE']._serialized_end=8544
  _globals['_STREAMHEALTHREQUEST']._serialized_start=8546
  _globals['_STREAMHEALTHREQUEST']._serialized_end=8567
  _globals['_REALTIMESTATS']._serialized_start=8570
  _globals['_REALTIMESTATS']._serialized_end=8774
  _globals['_AGGREGATESTATS']._serialized_start=8777
  _globals['_AGGREGATESTATS']._serialized_end=8929
  _globals['_STREAMHEALTHRESPONSE']._serialized_start=8932
  _globals['_STREAMHEALTHRESPONSE']._serialized_end=9147
  _globals['_TRANSACTIONMETADATA']._serialized_start=9150
  _globals['_TRANSACTIONMETADATA']._serialized_end=9284
# @@protoc_insertion_point(module_scope)
