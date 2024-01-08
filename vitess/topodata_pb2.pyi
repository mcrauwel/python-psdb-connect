from vitess import vttime_pb2 as _vttime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyspaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL: _ClassVar[KeyspaceType]
    SNAPSHOT: _ClassVar[KeyspaceType]

class KeyspaceIdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSET: _ClassVar[KeyspaceIdType]
    UINT64: _ClassVar[KeyspaceIdType]
    BYTES: _ClassVar[KeyspaceIdType]

class TabletType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[TabletType]
    PRIMARY: _ClassVar[TabletType]
    MASTER: _ClassVar[TabletType]
    REPLICA: _ClassVar[TabletType]
    RDONLY: _ClassVar[TabletType]
    BATCH: _ClassVar[TabletType]
    SPARE: _ClassVar[TabletType]
    EXPERIMENTAL: _ClassVar[TabletType]
    BACKUP: _ClassVar[TabletType]
    RESTORE: _ClassVar[TabletType]
    DRAINED: _ClassVar[TabletType]
NORMAL: KeyspaceType
SNAPSHOT: KeyspaceType
UNSET: KeyspaceIdType
UINT64: KeyspaceIdType
BYTES: KeyspaceIdType
UNKNOWN: TabletType
PRIMARY: TabletType
MASTER: TabletType
REPLICA: TabletType
RDONLY: TabletType
BATCH: TabletType
SPARE: TabletType
EXPERIMENTAL: TabletType
BACKUP: TabletType
RESTORE: TabletType
DRAINED: TabletType

class KeyRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: bytes
    end: bytes
    def __init__(self, start: _Optional[bytes] = ..., end: _Optional[bytes] = ...) -> None: ...

class TabletAlias(_message.Message):
    __slots__ = ("cell", "uid")
    CELL_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    cell: str
    uid: int
    def __init__(self, cell: _Optional[str] = ..., uid: _Optional[int] = ...) -> None: ...

class Tablet(_message.Message):
    __slots__ = ("alias", "hostname", "port_map", "keyspace", "shard", "key_range", "type", "db_name_override", "tags", "mysql_hostname", "mysql_port", "primary_term_start_time", "db_server_version", "default_conn_collation")
    class PortMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_MAP_FIELD_NUMBER: _ClassVar[int]
    KEYSPACE_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    KEY_RANGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MYSQL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    MYSQL_PORT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TERM_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DB_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONN_COLLATION_FIELD_NUMBER: _ClassVar[int]
    alias: TabletAlias
    hostname: str
    port_map: _containers.ScalarMap[str, int]
    keyspace: str
    shard: str
    key_range: KeyRange
    type: TabletType
    db_name_override: str
    tags: _containers.ScalarMap[str, str]
    mysql_hostname: str
    mysql_port: int
    primary_term_start_time: _vttime_pb2.Time
    db_server_version: str
    default_conn_collation: int
    def __init__(self, alias: _Optional[_Union[TabletAlias, _Mapping]] = ..., hostname: _Optional[str] = ..., port_map: _Optional[_Mapping[str, int]] = ..., keyspace: _Optional[str] = ..., shard: _Optional[str] = ..., key_range: _Optional[_Union[KeyRange, _Mapping]] = ..., type: _Optional[_Union[TabletType, str]] = ..., db_name_override: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., mysql_hostname: _Optional[str] = ..., mysql_port: _Optional[int] = ..., primary_term_start_time: _Optional[_Union[_vttime_pb2.Time, _Mapping]] = ..., db_server_version: _Optional[str] = ..., default_conn_collation: _Optional[int] = ...) -> None: ...

class Shard(_message.Message):
    __slots__ = ("primary_alias", "primary_term_start_time", "key_range", "source_shards", "tablet_controls", "is_primary_serving")
    class SourceShard(_message.Message):
        __slots__ = ("uid", "keyspace", "shard", "key_range", "tables")
        UID_FIELD_NUMBER: _ClassVar[int]
        KEYSPACE_FIELD_NUMBER: _ClassVar[int]
        SHARD_FIELD_NUMBER: _ClassVar[int]
        KEY_RANGE_FIELD_NUMBER: _ClassVar[int]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        uid: int
        keyspace: str
        shard: str
        key_range: KeyRange
        tables: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, uid: _Optional[int] = ..., keyspace: _Optional[str] = ..., shard: _Optional[str] = ..., key_range: _Optional[_Union[KeyRange, _Mapping]] = ..., tables: _Optional[_Iterable[str]] = ...) -> None: ...
    class TabletControl(_message.Message):
        __slots__ = ("tablet_type", "cells", "denied_tables", "frozen")
        TABLET_TYPE_FIELD_NUMBER: _ClassVar[int]
        CELLS_FIELD_NUMBER: _ClassVar[int]
        DENIED_TABLES_FIELD_NUMBER: _ClassVar[int]
        FROZEN_FIELD_NUMBER: _ClassVar[int]
        tablet_type: TabletType
        cells: _containers.RepeatedScalarFieldContainer[str]
        denied_tables: _containers.RepeatedScalarFieldContainer[str]
        frozen: bool
        def __init__(self, tablet_type: _Optional[_Union[TabletType, str]] = ..., cells: _Optional[_Iterable[str]] = ..., denied_tables: _Optional[_Iterable[str]] = ..., frozen: bool = ...) -> None: ...
    PRIMARY_ALIAS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TERM_START_TIME_FIELD_NUMBER: _ClassVar[int]
    KEY_RANGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SHARDS_FIELD_NUMBER: _ClassVar[int]
    TABLET_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_SERVING_FIELD_NUMBER: _ClassVar[int]
    primary_alias: TabletAlias
    primary_term_start_time: _vttime_pb2.Time
    key_range: KeyRange
    source_shards: _containers.RepeatedCompositeFieldContainer[Shard.SourceShard]
    tablet_controls: _containers.RepeatedCompositeFieldContainer[Shard.TabletControl]
    is_primary_serving: bool
    def __init__(self, primary_alias: _Optional[_Union[TabletAlias, _Mapping]] = ..., primary_term_start_time: _Optional[_Union[_vttime_pb2.Time, _Mapping]] = ..., key_range: _Optional[_Union[KeyRange, _Mapping]] = ..., source_shards: _Optional[_Iterable[_Union[Shard.SourceShard, _Mapping]]] = ..., tablet_controls: _Optional[_Iterable[_Union[Shard.TabletControl, _Mapping]]] = ..., is_primary_serving: bool = ...) -> None: ...

class Keyspace(_message.Message):
    __slots__ = ("sharding_column_name", "sharding_column_type", "served_froms", "keyspace_type", "base_keyspace", "snapshot_time")
    class ServedFrom(_message.Message):
        __slots__ = ("tablet_type", "cells", "keyspace")
        TABLET_TYPE_FIELD_NUMBER: _ClassVar[int]
        CELLS_FIELD_NUMBER: _ClassVar[int]
        KEYSPACE_FIELD_NUMBER: _ClassVar[int]
        tablet_type: TabletType
        cells: _containers.RepeatedScalarFieldContainer[str]
        keyspace: str
        def __init__(self, tablet_type: _Optional[_Union[TabletType, str]] = ..., cells: _Optional[_Iterable[str]] = ..., keyspace: _Optional[str] = ...) -> None: ...
    SHARDING_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARDING_COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVED_FROMS_FIELD_NUMBER: _ClassVar[int]
    KEYSPACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_KEYSPACE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    sharding_column_name: str
    sharding_column_type: KeyspaceIdType
    served_froms: _containers.RepeatedCompositeFieldContainer[Keyspace.ServedFrom]
    keyspace_type: KeyspaceType
    base_keyspace: str
    snapshot_time: _vttime_pb2.Time
    def __init__(self, sharding_column_name: _Optional[str] = ..., sharding_column_type: _Optional[_Union[KeyspaceIdType, str]] = ..., served_froms: _Optional[_Iterable[_Union[Keyspace.ServedFrom, _Mapping]]] = ..., keyspace_type: _Optional[_Union[KeyspaceType, str]] = ..., base_keyspace: _Optional[str] = ..., snapshot_time: _Optional[_Union[_vttime_pb2.Time, _Mapping]] = ...) -> None: ...

class ShardReplication(_message.Message):
    __slots__ = ("nodes",)
    class Node(_message.Message):
        __slots__ = ("tablet_alias",)
        TABLET_ALIAS_FIELD_NUMBER: _ClassVar[int]
        tablet_alias: TabletAlias
        def __init__(self, tablet_alias: _Optional[_Union[TabletAlias, _Mapping]] = ...) -> None: ...
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ShardReplication.Node]
    def __init__(self, nodes: _Optional[_Iterable[_Union[ShardReplication.Node, _Mapping]]] = ...) -> None: ...

class ShardReference(_message.Message):
    __slots__ = ("name", "key_range")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_RANGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_range: KeyRange
    def __init__(self, name: _Optional[str] = ..., key_range: _Optional[_Union[KeyRange, _Mapping]] = ...) -> None: ...

class ShardTabletControl(_message.Message):
    __slots__ = ("name", "key_range", "query_service_disabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_RANGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_SERVICE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_range: KeyRange
    query_service_disabled: bool
    def __init__(self, name: _Optional[str] = ..., key_range: _Optional[_Union[KeyRange, _Mapping]] = ..., query_service_disabled: bool = ...) -> None: ...

class SrvKeyspace(_message.Message):
    __slots__ = ("partitions", "sharding_column_name", "sharding_column_type", "served_from")
    class KeyspacePartition(_message.Message):
        __slots__ = ("served_type", "shard_references", "shard_tablet_controls")
        SERVED_TYPE_FIELD_NUMBER: _ClassVar[int]
        SHARD_REFERENCES_FIELD_NUMBER: _ClassVar[int]
        SHARD_TABLET_CONTROLS_FIELD_NUMBER: _ClassVar[int]
        served_type: TabletType
        shard_references: _containers.RepeatedCompositeFieldContainer[ShardReference]
        shard_tablet_controls: _containers.RepeatedCompositeFieldContainer[ShardTabletControl]
        def __init__(self, served_type: _Optional[_Union[TabletType, str]] = ..., shard_references: _Optional[_Iterable[_Union[ShardReference, _Mapping]]] = ..., shard_tablet_controls: _Optional[_Iterable[_Union[ShardTabletControl, _Mapping]]] = ...) -> None: ...
    class ServedFrom(_message.Message):
        __slots__ = ("tablet_type", "keyspace")
        TABLET_TYPE_FIELD_NUMBER: _ClassVar[int]
        KEYSPACE_FIELD_NUMBER: _ClassVar[int]
        tablet_type: TabletType
        keyspace: str
        def __init__(self, tablet_type: _Optional[_Union[TabletType, str]] = ..., keyspace: _Optional[str] = ...) -> None: ...
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SHARDING_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARDING_COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVED_FROM_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedCompositeFieldContainer[SrvKeyspace.KeyspacePartition]
    sharding_column_name: str
    sharding_column_type: KeyspaceIdType
    served_from: _containers.RepeatedCompositeFieldContainer[SrvKeyspace.ServedFrom]
    def __init__(self, partitions: _Optional[_Iterable[_Union[SrvKeyspace.KeyspacePartition, _Mapping]]] = ..., sharding_column_name: _Optional[str] = ..., sharding_column_type: _Optional[_Union[KeyspaceIdType, str]] = ..., served_from: _Optional[_Iterable[_Union[SrvKeyspace.ServedFrom, _Mapping]]] = ...) -> None: ...

class CellInfo(_message.Message):
    __slots__ = ("server_address", "root")
    SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    server_address: str
    root: str
    def __init__(self, server_address: _Optional[str] = ..., root: _Optional[str] = ...) -> None: ...

class CellsAlias(_message.Message):
    __slots__ = ("cells",)
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cells: _Optional[_Iterable[str]] = ...) -> None: ...

class TopoConfig(_message.Message):
    __slots__ = ("topo_type", "server", "root")
    TOPO_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    topo_type: str
    server: str
    root: str
    def __init__(self, topo_type: _Optional[str] = ..., server: _Optional[str] = ..., root: _Optional[str] = ...) -> None: ...

class ExternalVitessCluster(_message.Message):
    __slots__ = ("topo_config",)
    TOPO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    topo_config: TopoConfig
    def __init__(self, topo_config: _Optional[_Union[TopoConfig, _Mapping]] = ...) -> None: ...

class ExternalClusters(_message.Message):
    __slots__ = ("vitess_cluster",)
    VITESS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    vitess_cluster: _containers.RepeatedCompositeFieldContainer[ExternalVitessCluster]
    def __init__(self, vitess_cluster: _Optional[_Iterable[_Union[ExternalVitessCluster, _Mapping]]] = ...) -> None: ...
