# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vitess/vttime.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13vitess/vttime.proto\x12\x06vttime\",\n\x04Time\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\x13\n\x0bnanoseconds\x18\x02 \x01(\x05\"*\n\x08\x44uration\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\x42%Z#vitess.io/vitess/go/vt/proto/vttimeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vitess.vttime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#vitess.io/vitess/go/vt/proto/vttime'
  _globals['_TIME']._serialized_start=31
  _globals['_TIME']._serialized_end=75
  _globals['_DURATION']._serialized_start=77
  _globals['_DURATION']._serialized_end=119
# @@protoc_insertion_point(module_scope)