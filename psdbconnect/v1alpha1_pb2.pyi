from vitess import query_pb2 as _query_pb2
from vitess import vtrpc_pb2 as _vtrpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TabletType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    replica: _ClassVar[TabletType]
    primary: _ClassVar[TabletType]
    batch: _ClassVar[TabletType]
replica: TabletType
primary: TabletType
batch: TabletType

class SyncRequest(_message.Message):
    __slots__ = ("table_name", "cursor", "tablet_type", "include_inserts", "include_updates", "include_deletes", "columns", "cells")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    TABLET_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INSERTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    cursor: TableCursor
    tablet_type: TabletType
    include_inserts: bool
    include_updates: bool
    include_deletes: bool
    columns: _containers.RepeatedScalarFieldContainer[str]
    cells: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, table_name: _Optional[str] = ..., cursor: _Optional[_Union[TableCursor, _Mapping]] = ..., tablet_type: _Optional[_Union[TabletType, str]] = ..., include_inserts: bool = ..., include_updates: bool = ..., include_deletes: bool = ..., columns: _Optional[_Iterable[str]] = ..., cells: _Optional[_Iterable[str]] = ...) -> None: ...

class DeletedRow(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _query_pb2.QueryResult
    def __init__(self, result: _Optional[_Union[_query_pb2.QueryResult, _Mapping]] = ...) -> None: ...

class UpdatedRow(_message.Message):
    __slots__ = ("before", "after")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    before: _query_pb2.QueryResult
    after: _query_pb2.QueryResult
    def __init__(self, before: _Optional[_Union[_query_pb2.QueryResult, _Mapping]] = ..., after: _Optional[_Union[_query_pb2.QueryResult, _Mapping]] = ...) -> None: ...

class SyncResponse(_message.Message):
    __slots__ = ("result", "cursor", "error", "deletes", "updates")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETES_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_query_pb2.QueryResult]
    cursor: TableCursor
    error: _vtrpc_pb2.RPCError
    deletes: _containers.RepeatedCompositeFieldContainer[DeletedRow]
    updates: _containers.RepeatedCompositeFieldContainer[UpdatedRow]
    def __init__(self, result: _Optional[_Iterable[_Union[_query_pb2.QueryResult, _Mapping]]] = ..., cursor: _Optional[_Union[TableCursor, _Mapping]] = ..., error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., deletes: _Optional[_Iterable[_Union[DeletedRow, _Mapping]]] = ..., updates: _Optional[_Iterable[_Union[UpdatedRow, _Mapping]]] = ...) -> None: ...

class TableCursor(_message.Message):
    __slots__ = ("shard", "keyspace", "position", "last_known_pk")
    SHARD_FIELD_NUMBER: _ClassVar[int]
    KEYSPACE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_PK_FIELD_NUMBER: _ClassVar[int]
    shard: str
    keyspace: str
    position: str
    last_known_pk: _query_pb2.QueryResult
    def __init__(self, shard: _Optional[str] = ..., keyspace: _Optional[str] = ..., position: _Optional[str] = ..., last_known_pk: _Optional[_Union[_query_pb2.QueryResult, _Mapping]] = ...) -> None: ...
