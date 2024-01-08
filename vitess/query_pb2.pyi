from vitess import topodata_pb2 as _topodata_pb2
from vitess import vtrpc_pb2 as _vtrpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MySqlFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMPTY: _ClassVar[MySqlFlag]
    NOT_NULL_FLAG: _ClassVar[MySqlFlag]
    PRI_KEY_FLAG: _ClassVar[MySqlFlag]
    UNIQUE_KEY_FLAG: _ClassVar[MySqlFlag]
    MULTIPLE_KEY_FLAG: _ClassVar[MySqlFlag]
    BLOB_FLAG: _ClassVar[MySqlFlag]
    UNSIGNED_FLAG: _ClassVar[MySqlFlag]
    ZEROFILL_FLAG: _ClassVar[MySqlFlag]
    BINARY_FLAG: _ClassVar[MySqlFlag]
    ENUM_FLAG: _ClassVar[MySqlFlag]
    AUTO_INCREMENT_FLAG: _ClassVar[MySqlFlag]
    TIMESTAMP_FLAG: _ClassVar[MySqlFlag]
    SET_FLAG: _ClassVar[MySqlFlag]
    NO_DEFAULT_VALUE_FLAG: _ClassVar[MySqlFlag]
    ON_UPDATE_NOW_FLAG: _ClassVar[MySqlFlag]
    NUM_FLAG: _ClassVar[MySqlFlag]
    PART_KEY_FLAG: _ClassVar[MySqlFlag]
    GROUP_FLAG: _ClassVar[MySqlFlag]
    UNIQUE_FLAG: _ClassVar[MySqlFlag]
    BINCMP_FLAG: _ClassVar[MySqlFlag]

class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[Flag]
    ISINTEGRAL: _ClassVar[Flag]
    ISUNSIGNED: _ClassVar[Flag]
    ISFLOAT: _ClassVar[Flag]
    ISQUOTED: _ClassVar[Flag]
    ISTEXT: _ClassVar[Flag]
    ISBINARY: _ClassVar[Flag]

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NULL_TYPE: _ClassVar[Type]
    INT8: _ClassVar[Type]
    UINT8: _ClassVar[Type]
    INT16: _ClassVar[Type]
    UINT16: _ClassVar[Type]
    INT24: _ClassVar[Type]
    UINT24: _ClassVar[Type]
    INT32: _ClassVar[Type]
    UINT32: _ClassVar[Type]
    INT64: _ClassVar[Type]
    UINT64: _ClassVar[Type]
    FLOAT32: _ClassVar[Type]
    FLOAT64: _ClassVar[Type]
    TIMESTAMP: _ClassVar[Type]
    DATE: _ClassVar[Type]
    TIME: _ClassVar[Type]
    DATETIME: _ClassVar[Type]
    YEAR: _ClassVar[Type]
    DECIMAL: _ClassVar[Type]
    TEXT: _ClassVar[Type]
    BLOB: _ClassVar[Type]
    VARCHAR: _ClassVar[Type]
    VARBINARY: _ClassVar[Type]
    CHAR: _ClassVar[Type]
    BINARY: _ClassVar[Type]
    BIT: _ClassVar[Type]
    ENUM: _ClassVar[Type]
    SET: _ClassVar[Type]
    TUPLE: _ClassVar[Type]
    GEOMETRY: _ClassVar[Type]
    JSON: _ClassVar[Type]
    EXPRESSION: _ClassVar[Type]
    HEXNUM: _ClassVar[Type]
    HEXVAL: _ClassVar[Type]

class TransactionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[TransactionState]
    PREPARE: _ClassVar[TransactionState]
    COMMIT: _ClassVar[TransactionState]
    ROLLBACK: _ClassVar[TransactionState]
EMPTY: MySqlFlag
NOT_NULL_FLAG: MySqlFlag
PRI_KEY_FLAG: MySqlFlag
UNIQUE_KEY_FLAG: MySqlFlag
MULTIPLE_KEY_FLAG: MySqlFlag
BLOB_FLAG: MySqlFlag
UNSIGNED_FLAG: MySqlFlag
ZEROFILL_FLAG: MySqlFlag
BINARY_FLAG: MySqlFlag
ENUM_FLAG: MySqlFlag
AUTO_INCREMENT_FLAG: MySqlFlag
TIMESTAMP_FLAG: MySqlFlag
SET_FLAG: MySqlFlag
NO_DEFAULT_VALUE_FLAG: MySqlFlag
ON_UPDATE_NOW_FLAG: MySqlFlag
NUM_FLAG: MySqlFlag
PART_KEY_FLAG: MySqlFlag
GROUP_FLAG: MySqlFlag
UNIQUE_FLAG: MySqlFlag
BINCMP_FLAG: MySqlFlag
NONE: Flag
ISINTEGRAL: Flag
ISUNSIGNED: Flag
ISFLOAT: Flag
ISQUOTED: Flag
ISTEXT: Flag
ISBINARY: Flag
NULL_TYPE: Type
INT8: Type
UINT8: Type
INT16: Type
UINT16: Type
INT24: Type
UINT24: Type
INT32: Type
UINT32: Type
INT64: Type
UINT64: Type
FLOAT32: Type
FLOAT64: Type
TIMESTAMP: Type
DATE: Type
TIME: Type
DATETIME: Type
YEAR: Type
DECIMAL: Type
TEXT: Type
BLOB: Type
VARCHAR: Type
VARBINARY: Type
CHAR: Type
BINARY: Type
BIT: Type
ENUM: Type
SET: Type
TUPLE: Type
GEOMETRY: Type
JSON: Type
EXPRESSION: Type
HEXNUM: Type
HEXVAL: Type
UNKNOWN: TransactionState
PREPARE: TransactionState
COMMIT: TransactionState
ROLLBACK: TransactionState

class Target(_message.Message):
    __slots__ = ("keyspace", "shard", "tablet_type", "cell")
    KEYSPACE_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    TABLET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    keyspace: str
    shard: str
    tablet_type: _topodata_pb2.TabletType
    cell: str
    def __init__(self, keyspace: _Optional[str] = ..., shard: _Optional[str] = ..., tablet_type: _Optional[_Union[_topodata_pb2.TabletType, str]] = ..., cell: _Optional[str] = ...) -> None: ...

class VTGateCallerID(_message.Message):
    __slots__ = ("username", "groups")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    username: str
    groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, username: _Optional[str] = ..., groups: _Optional[_Iterable[str]] = ...) -> None: ...

class EventToken(_message.Message):
    __slots__ = ("timestamp", "shard", "position")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    shard: str
    position: str
    def __init__(self, timestamp: _Optional[int] = ..., shard: _Optional[str] = ..., position: _Optional[str] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: Type
    value: bytes
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., value: _Optional[bytes] = ...) -> None: ...

class BindVariable(_message.Message):
    __slots__ = ("type", "value", "values")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    type: Type
    value: bytes
    values: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., value: _Optional[bytes] = ..., values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class BoundQuery(_message.Message):
    __slots__ = ("sql", "bind_variables")
    class BindVariablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BindVariable
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BindVariable, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    BIND_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    sql: str
    bind_variables: _containers.MessageMap[str, BindVariable]
    def __init__(self, sql: _Optional[str] = ..., bind_variables: _Optional[_Mapping[str, BindVariable]] = ...) -> None: ...

class ExecuteOptions(_message.Message):
    __slots__ = ("included_fields", "client_found_rows", "workload", "sql_select_limit", "transaction_isolation", "skip_query_plan_cache", "planner_version", "has_created_temp_tables")
    class IncludedFields(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_AND_NAME: _ClassVar[ExecuteOptions.IncludedFields]
        TYPE_ONLY: _ClassVar[ExecuteOptions.IncludedFields]
        ALL: _ClassVar[ExecuteOptions.IncludedFields]
    TYPE_AND_NAME: ExecuteOptions.IncludedFields
    TYPE_ONLY: ExecuteOptions.IncludedFields
    ALL: ExecuteOptions.IncludedFields
    class Workload(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExecuteOptions.Workload]
        OLTP: _ClassVar[ExecuteOptions.Workload]
        OLAP: _ClassVar[ExecuteOptions.Workload]
        DBA: _ClassVar[ExecuteOptions.Workload]
    UNSPECIFIED: ExecuteOptions.Workload
    OLTP: ExecuteOptions.Workload
    OLAP: ExecuteOptions.Workload
    DBA: ExecuteOptions.Workload
    class TransactionIsolation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ExecuteOptions.TransactionIsolation]
        REPEATABLE_READ: _ClassVar[ExecuteOptions.TransactionIsolation]
        READ_COMMITTED: _ClassVar[ExecuteOptions.TransactionIsolation]
        READ_UNCOMMITTED: _ClassVar[ExecuteOptions.TransactionIsolation]
        SERIALIZABLE: _ClassVar[ExecuteOptions.TransactionIsolation]
        CONSISTENT_SNAPSHOT_READ_ONLY: _ClassVar[ExecuteOptions.TransactionIsolation]
        AUTOCOMMIT: _ClassVar[ExecuteOptions.TransactionIsolation]
    DEFAULT: ExecuteOptions.TransactionIsolation
    REPEATABLE_READ: ExecuteOptions.TransactionIsolation
    READ_COMMITTED: ExecuteOptions.TransactionIsolation
    READ_UNCOMMITTED: ExecuteOptions.TransactionIsolation
    SERIALIZABLE: ExecuteOptions.TransactionIsolation
    CONSISTENT_SNAPSHOT_READ_ONLY: ExecuteOptions.TransactionIsolation
    AUTOCOMMIT: ExecuteOptions.TransactionIsolation
    class PlannerVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_PLANNER: _ClassVar[ExecuteOptions.PlannerVersion]
        V3: _ClassVar[ExecuteOptions.PlannerVersion]
        Gen4: _ClassVar[ExecuteOptions.PlannerVersion]
        Gen4Greedy: _ClassVar[ExecuteOptions.PlannerVersion]
        Gen4Left2Right: _ClassVar[ExecuteOptions.PlannerVersion]
        Gen4WithFallback: _ClassVar[ExecuteOptions.PlannerVersion]
        Gen4CompareV3: _ClassVar[ExecuteOptions.PlannerVersion]
    DEFAULT_PLANNER: ExecuteOptions.PlannerVersion
    V3: ExecuteOptions.PlannerVersion
    Gen4: ExecuteOptions.PlannerVersion
    Gen4Greedy: ExecuteOptions.PlannerVersion
    Gen4Left2Right: ExecuteOptions.PlannerVersion
    Gen4WithFallback: ExecuteOptions.PlannerVersion
    Gen4CompareV3: ExecuteOptions.PlannerVersion
    INCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FOUND_ROWS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    SQL_SELECT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ISOLATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_QUERY_PLAN_CACHE_FIELD_NUMBER: _ClassVar[int]
    PLANNER_VERSION_FIELD_NUMBER: _ClassVar[int]
    HAS_CREATED_TEMP_TABLES_FIELD_NUMBER: _ClassVar[int]
    included_fields: ExecuteOptions.IncludedFields
    client_found_rows: bool
    workload: ExecuteOptions.Workload
    sql_select_limit: int
    transaction_isolation: ExecuteOptions.TransactionIsolation
    skip_query_plan_cache: bool
    planner_version: ExecuteOptions.PlannerVersion
    has_created_temp_tables: bool
    def __init__(self, included_fields: _Optional[_Union[ExecuteOptions.IncludedFields, str]] = ..., client_found_rows: bool = ..., workload: _Optional[_Union[ExecuteOptions.Workload, str]] = ..., sql_select_limit: _Optional[int] = ..., transaction_isolation: _Optional[_Union[ExecuteOptions.TransactionIsolation, str]] = ..., skip_query_plan_cache: bool = ..., planner_version: _Optional[_Union[ExecuteOptions.PlannerVersion, str]] = ..., has_created_temp_tables: bool = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("name", "type", "table", "org_table", "database", "org_name", "column_length", "charset", "decimals", "flags", "column_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ORG_TABLE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CHARSET_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Type
    table: str
    org_table: str
    database: str
    org_name: str
    column_length: int
    charset: int
    decimals: int
    flags: int
    column_type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[Type, str]] = ..., table: _Optional[str] = ..., org_table: _Optional[str] = ..., database: _Optional[str] = ..., org_name: _Optional[str] = ..., column_length: _Optional[int] = ..., charset: _Optional[int] = ..., decimals: _Optional[int] = ..., flags: _Optional[int] = ..., column_type: _Optional[str] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ("lengths", "values")
    LENGTHS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    lengths: _containers.RepeatedScalarFieldContainer[int]
    values: bytes
    def __init__(self, lengths: _Optional[_Iterable[int]] = ..., values: _Optional[bytes] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ("fields", "rows_affected", "insert_id", "rows")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ROWS_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    INSERT_ID_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    rows_affected: int
    insert_id: int
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    def __init__(self, fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., rows_affected: _Optional[int] = ..., insert_id: _Optional[int] = ..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ...) -> None: ...

class QueryWarning(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class StreamEvent(_message.Message):
    __slots__ = ("statements", "event_token")
    class Statement(_message.Message):
        __slots__ = ("category", "table_name", "primary_key_fields", "primary_key_values", "sql")
        class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Error: _ClassVar[StreamEvent.Statement.Category]
            DML: _ClassVar[StreamEvent.Statement.Category]
            DDL: _ClassVar[StreamEvent.Statement.Category]
        Error: StreamEvent.Statement.Category
        DML: StreamEvent.Statement.Category
        DDL: StreamEvent.Statement.Category
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_KEY_FIELDS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        SQL_FIELD_NUMBER: _ClassVar[int]
        category: StreamEvent.Statement.Category
        table_name: str
        primary_key_fields: _containers.RepeatedCompositeFieldContainer[Field]
        primary_key_values: _containers.RepeatedCompositeFieldContainer[Row]
        sql: bytes
        def __init__(self, category: _Optional[_Union[StreamEvent.Statement.Category, str]] = ..., table_name: _Optional[str] = ..., primary_key_fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., primary_key_values: _Optional[_Iterable[_Union[Row, _Mapping]]] = ..., sql: _Optional[bytes] = ...) -> None: ...
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    statements: _containers.RepeatedCompositeFieldContainer[StreamEvent.Statement]
    event_token: EventToken
    def __init__(self, statements: _Optional[_Iterable[_Union[StreamEvent.Statement, _Mapping]]] = ..., event_token: _Optional[_Union[EventToken, _Mapping]] = ...) -> None: ...

class ExecuteRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "query", "transaction_id", "options", "reserved_id")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    query: BoundQuery
    transaction_id: int
    options: ExecuteOptions
    reserved_id: int
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., query: _Optional[_Union[BoundQuery, _Mapping]] = ..., transaction_id: _Optional[int] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ..., reserved_id: _Optional[int] = ...) -> None: ...

class ExecuteResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: QueryResult
    def __init__(self, result: _Optional[_Union[QueryResult, _Mapping]] = ...) -> None: ...

class ResultWithError(_message.Message):
    __slots__ = ("error", "result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _vtrpc_pb2.RPCError
    result: QueryResult
    def __init__(self, error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., result: _Optional[_Union[QueryResult, _Mapping]] = ...) -> None: ...

class ExecuteBatchRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "queries", "as_transaction", "transaction_id", "options")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    AS_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    queries: _containers.RepeatedCompositeFieldContainer[BoundQuery]
    as_transaction: bool
    transaction_id: int
    options: ExecuteOptions
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., queries: _Optional[_Iterable[_Union[BoundQuery, _Mapping]]] = ..., as_transaction: bool = ..., transaction_id: _Optional[int] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ...) -> None: ...

class ExecuteBatchResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[QueryResult]
    def __init__(self, results: _Optional[_Iterable[_Union[QueryResult, _Mapping]]] = ...) -> None: ...

class StreamExecuteRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "query", "options", "transaction_id")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    query: BoundQuery
    options: ExecuteOptions
    transaction_id: int
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., query: _Optional[_Union[BoundQuery, _Mapping]] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ..., transaction_id: _Optional[int] = ...) -> None: ...

class StreamExecuteResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: QueryResult
    def __init__(self, result: _Optional[_Union[QueryResult, _Mapping]] = ...) -> None: ...

class BeginRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "options")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    options: ExecuteOptions
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ...) -> None: ...

class BeginResponse(_message.Message):
    __slots__ = ("transaction_id", "tablet_alias")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    transaction_id: int
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, transaction_id: _Optional[int] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class CommitRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ...) -> None: ...

class CommitResponse(_message.Message):
    __slots__ = ("reserved_id",)
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    reserved_id: int
    def __init__(self, reserved_id: _Optional[int] = ...) -> None: ...

class RollbackRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ...) -> None: ...

class RollbackResponse(_message.Message):
    __slots__ = ("reserved_id",)
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    reserved_id: int
    def __init__(self, reserved_id: _Optional[int] = ...) -> None: ...

class PrepareRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ..., dtid: _Optional[str] = ...) -> None: ...

class PrepareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommitPreparedRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., dtid: _Optional[str] = ...) -> None: ...

class CommitPreparedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollbackPreparedRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ..., dtid: _Optional[str] = ...) -> None: ...

class RollbackPreparedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTransactionRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "dtid", "participants")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    dtid: str
    participants: _containers.RepeatedCompositeFieldContainer[Target]
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., dtid: _Optional[str] = ..., participants: _Optional[_Iterable[_Union[Target, _Mapping]]] = ...) -> None: ...

class CreateTransactionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartCommitRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ..., dtid: _Optional[str] = ...) -> None: ...

class StartCommitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetRollbackRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ..., dtid: _Optional[str] = ...) -> None: ...

class SetRollbackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConcludeTransactionRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., dtid: _Optional[str] = ...) -> None: ...

class ConcludeTransactionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadTransactionRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "dtid")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DTID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    dtid: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., dtid: _Optional[str] = ...) -> None: ...

class ReadTransactionResponse(_message.Message):
    __slots__ = ("metadata",)
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: TransactionMetadata
    def __init__(self, metadata: _Optional[_Union[TransactionMetadata, _Mapping]] = ...) -> None: ...

class BeginExecuteRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "query", "options", "reserved_id", "pre_queries")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    query: BoundQuery
    options: ExecuteOptions
    reserved_id: int
    pre_queries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., query: _Optional[_Union[BoundQuery, _Mapping]] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ..., reserved_id: _Optional[int] = ..., pre_queries: _Optional[_Iterable[str]] = ...) -> None: ...

class BeginExecuteResponse(_message.Message):
    __slots__ = ("error", "result", "transaction_id", "tablet_alias")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    error: _vtrpc_pb2.RPCError
    result: QueryResult
    transaction_id: int
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., result: _Optional[_Union[QueryResult, _Mapping]] = ..., transaction_id: _Optional[int] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class BeginExecuteBatchRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "queries", "as_transaction", "options")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    AS_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    queries: _containers.RepeatedCompositeFieldContainer[BoundQuery]
    as_transaction: bool
    options: ExecuteOptions
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., queries: _Optional[_Iterable[_Union[BoundQuery, _Mapping]]] = ..., as_transaction: bool = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ...) -> None: ...

class BeginExecuteBatchResponse(_message.Message):
    __slots__ = ("error", "results", "transaction_id", "tablet_alias")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    error: _vtrpc_pb2.RPCError
    results: _containers.RepeatedCompositeFieldContainer[QueryResult]
    transaction_id: int
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., results: _Optional[_Iterable[_Union[QueryResult, _Mapping]]] = ..., transaction_id: _Optional[int] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class BeginStreamExecuteRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "query", "options", "pre_queries")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    query: BoundQuery
    options: ExecuteOptions
    pre_queries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., query: _Optional[_Union[BoundQuery, _Mapping]] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ..., pre_queries: _Optional[_Iterable[str]] = ...) -> None: ...

class BeginStreamExecuteResponse(_message.Message):
    __slots__ = ("error", "result", "transaction_id", "tablet_alias")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    error: _vtrpc_pb2.RPCError
    result: QueryResult
    transaction_id: int
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., result: _Optional[_Union[QueryResult, _Mapping]] = ..., transaction_id: _Optional[int] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class MessageStreamRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "name")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    name: str
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class MessageStreamResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: QueryResult
    def __init__(self, result: _Optional[_Union[QueryResult, _Mapping]] = ...) -> None: ...

class MessageAckRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "name", "ids")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    name: str
    ids: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., name: _Optional[str] = ..., ids: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class MessageAckResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: QueryResult
    def __init__(self, result: _Optional[_Union[QueryResult, _Mapping]] = ...) -> None: ...

class ReserveExecuteRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "query", "transaction_id", "options", "pre_queries")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    query: BoundQuery
    transaction_id: int
    options: ExecuteOptions
    pre_queries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., query: _Optional[_Union[BoundQuery, _Mapping]] = ..., transaction_id: _Optional[int] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ..., pre_queries: _Optional[_Iterable[str]] = ...) -> None: ...

class ReserveExecuteResponse(_message.Message):
    __slots__ = ("error", "result", "reserved_id", "tablet_alias")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    error: _vtrpc_pb2.RPCError
    result: QueryResult
    reserved_id: int
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., result: _Optional[_Union[QueryResult, _Mapping]] = ..., reserved_id: _Optional[int] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class ReserveBeginExecuteRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "query", "options", "pre_queries", "post_begin_queries")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    POST_BEGIN_QUERIES_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    query: BoundQuery
    options: ExecuteOptions
    pre_queries: _containers.RepeatedScalarFieldContainer[str]
    post_begin_queries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., query: _Optional[_Union[BoundQuery, _Mapping]] = ..., options: _Optional[_Union[ExecuteOptions, _Mapping]] = ..., pre_queries: _Optional[_Iterable[str]] = ..., post_begin_queries: _Optional[_Iterable[str]] = ...) -> None: ...

class ReserveBeginExecuteResponse(_message.Message):
    __slots__ = ("error", "result", "transaction_id", "reserved_id", "tablet_alias")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    error: _vtrpc_pb2.RPCError
    result: QueryResult
    transaction_id: int
    reserved_id: int
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, error: _Optional[_Union[_vtrpc_pb2.RPCError, _Mapping]] = ..., result: _Optional[_Union[QueryResult, _Mapping]] = ..., transaction_id: _Optional[int] = ..., reserved_id: _Optional[int] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class ReleaseRequest(_message.Message):
    __slots__ = ("effective_caller_id", "immediate_caller_id", "target", "transaction_id", "reserved_id")
    EFFECTIVE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ID_FIELD_NUMBER: _ClassVar[int]
    effective_caller_id: _vtrpc_pb2.CallerID
    immediate_caller_id: VTGateCallerID
    target: Target
    transaction_id: int
    reserved_id: int
    def __init__(self, effective_caller_id: _Optional[_Union[_vtrpc_pb2.CallerID, _Mapping]] = ..., immediate_caller_id: _Optional[_Union[VTGateCallerID, _Mapping]] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., transaction_id: _Optional[int] = ..., reserved_id: _Optional[int] = ...) -> None: ...

class ReleaseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StreamHealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RealtimeStats(_message.Message):
    __slots__ = ("health_error", "replication_lag_seconds", "binlog_players_count", "filtered_replication_lag_seconds", "cpu_usage", "qps", "table_schema_changed")
    HEALTH_ERROR_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_LAG_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BINLOG_PLAYERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILTERED_REPLICATION_LAG_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    QPS_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCHEMA_CHANGED_FIELD_NUMBER: _ClassVar[int]
    health_error: str
    replication_lag_seconds: int
    binlog_players_count: int
    filtered_replication_lag_seconds: int
    cpu_usage: float
    qps: float
    table_schema_changed: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, health_error: _Optional[str] = ..., replication_lag_seconds: _Optional[int] = ..., binlog_players_count: _Optional[int] = ..., filtered_replication_lag_seconds: _Optional[int] = ..., cpu_usage: _Optional[float] = ..., qps: _Optional[float] = ..., table_schema_changed: _Optional[_Iterable[str]] = ...) -> None: ...

class AggregateStats(_message.Message):
    __slots__ = ("healthy_tablet_count", "unhealthy_tablet_count", "replication_lag_seconds_min", "replication_lag_seconds_max")
    HEALTHY_TABLET_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_TABLET_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_LAG_SECONDS_MIN_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_LAG_SECONDS_MAX_FIELD_NUMBER: _ClassVar[int]
    healthy_tablet_count: int
    unhealthy_tablet_count: int
    replication_lag_seconds_min: int
    replication_lag_seconds_max: int
    def __init__(self, healthy_tablet_count: _Optional[int] = ..., unhealthy_tablet_count: _Optional[int] = ..., replication_lag_seconds_min: _Optional[int] = ..., replication_lag_seconds_max: _Optional[int] = ...) -> None: ...

class StreamHealthResponse(_message.Message):
    __slots__ = ("target", "serving", "tablet_externally_reparented_timestamp", "realtime_stats", "tablet_alias")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SERVING_FIELD_NUMBER: _ClassVar[int]
    TABLET_EXTERNALLY_REPARENTED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REALTIME_STATS_FIELD_NUMBER: _ClassVar[int]
    TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
    target: Target
    serving: bool
    tablet_externally_reparented_timestamp: int
    realtime_stats: RealtimeStats
    tablet_alias: _topodata_pb2.TabletAlias
    def __init__(self, target: _Optional[_Union[Target, _Mapping]] = ..., serving: bool = ..., tablet_externally_reparented_timestamp: _Optional[int] = ..., realtime_stats: _Optional[_Union[RealtimeStats, _Mapping]] = ..., tablet_alias: _Optional[_Union[_topodata_pb2.TabletAlias, _Mapping]] = ...) -> None: ...

class TransactionMetadata(_message.Message):
    __slots__ = ("dtid", "state", "time_created", "participants")
    DTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    dtid: str
    state: TransactionState
    time_created: int
    participants: _containers.RepeatedCompositeFieldContainer[Target]
    def __init__(self, dtid: _Optional[str] = ..., state: _Optional[_Union[TransactionState, str]] = ..., time_created: _Optional[int] = ..., participants: _Optional[_Iterable[_Union[Target, _Mapping]]] = ...) -> None: ...
