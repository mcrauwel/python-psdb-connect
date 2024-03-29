# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: psdbconnect/v1alpha1.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vitess import query_pb2 as vitess_dot_query__pb2
from vitess import vtrpc_pb2 as vitess_dot_vtrpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apsdbconnect/v1alpha1.proto\x12\x14psdbconnect.v1alpha1\x1a\x12vitess/query.proto\x1a\x12vitess/vtrpc.proto\"\xf6\x01\n\x0bSyncRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x31\n\x06\x63ursor\x18\x02 \x01(\x0b\x32!.psdbconnect.v1alpha1.TableCursor\x12\x35\n\x0btablet_type\x18\x03 \x01(\x0e\x32 .psdbconnect.v1alpha1.TabletType\x12\x17\n\x0finclude_inserts\x18\x04 \x01(\x08\x12\x17\n\x0finclude_updates\x18\x05 \x01(\x08\x12\x17\n\x0finclude_deletes\x18\x06 \x01(\x08\x12\x0f\n\x07\x63olumns\x18\x07 \x03(\t\x12\r\n\x05\x63\x65lls\x18\x08 \x03(\t\"0\n\nDeletedRow\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\x12.query.QueryResult\"S\n\nUpdatedRow\x12\"\n\x06\x62\x65\x66ore\x18\x01 \x01(\x0b\x32\x12.query.QueryResult\x12!\n\x05\x61\x66ter\x18\x02 \x01(\x0b\x32\x12.query.QueryResult\"\xeb\x01\n\x0cSyncResponse\x12\"\n\x06result\x18\x01 \x03(\x0b\x32\x12.query.QueryResult\x12\x31\n\x06\x63ursor\x18\x02 \x01(\x0b\x32!.psdbconnect.v1alpha1.TableCursor\x12\x1e\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x0f.vtrpc.RPCError\x12\x31\n\x07\x64\x65letes\x18\x04 \x03(\x0b\x32 .psdbconnect.v1alpha1.DeletedRow\x12\x31\n\x07updates\x18\x05 \x03(\x0b\x32 .psdbconnect.v1alpha1.UpdatedRow\"k\n\x0bTableCursor\x12\r\n\x05shard\x18\x01 \x01(\t\x12\x10\n\x08keyspace\x18\x02 \x01(\t\x12\x10\n\x08position\x18\x03 \x01(\t\x12)\n\rlast_known_pk\x18\x04 \x01(\x0b\x32\x12.query.QueryResult*1\n\nTabletType\x12\x0b\n\x07replica\x10\x00\x12\x0b\n\x07primary\x10\x01\x12\t\n\x05\x62\x61tch\x10\x02\x32\\\n\x07\x43onnect\x12Q\n\x04Sync\x12!.psdbconnect.v1alpha1.SyncRequest\x1a\".psdbconnect.v1alpha1.SyncResponse\"\x00\x30\x01\x42LZJgithub.com/planetscale/psdb/types/psdbconnect/v1alpha1;psdbconnectv1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'psdbconnect.v1alpha1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZJgithub.com/planetscale/psdb/types/psdbconnect/v1alpha1;psdbconnectv1alpha1'
  _globals['_TABLETTYPE']._serialized_start=823
  _globals['_TABLETTYPE']._serialized_end=872
  _globals['_SYNCREQUEST']._serialized_start=93
  _globals['_SYNCREQUEST']._serialized_end=339
  _globals['_DELETEDROW']._serialized_start=341
  _globals['_DELETEDROW']._serialized_end=389
  _globals['_UPDATEDROW']._serialized_start=391
  _globals['_UPDATEDROW']._serialized_end=474
  _globals['_SYNCRESPONSE']._serialized_start=477
  _globals['_SYNCRESPONSE']._serialized_end=712
  _globals['_TABLECURSOR']._serialized_start=714
  _globals['_TABLECURSOR']._serialized_end=821
  _globals['_CONNECT']._serialized_start=874
  _globals['_CONNECT']._serialized_end=966
# @@protoc_insertion_point(module_scope)
