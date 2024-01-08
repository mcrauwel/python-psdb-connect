from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileDescriptorSet(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _containers.RepeatedCompositeFieldContainer[FileDescriptorProto]
    def __init__(self, file: _Optional[_Iterable[_Union[FileDescriptorProto, _Mapping]]] = ...) -> None: ...

class FileDescriptorProto(_message.Message):
    __slots__ = ("name", "package", "dependency", "public_dependency", "weak_dependency", "message_type", "enum_type", "service", "extension", "options", "source_code_info", "syntax")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    WEAK_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_INFO_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    package: str
    dependency: _containers.RepeatedScalarFieldContainer[str]
    public_dependency: _containers.RepeatedScalarFieldContainer[int]
    weak_dependency: _containers.RepeatedScalarFieldContainer[int]
    message_type: _containers.RepeatedCompositeFieldContainer[DescriptorProto]
    enum_type: _containers.RepeatedCompositeFieldContainer[EnumDescriptorProto]
    service: _containers.RepeatedCompositeFieldContainer[ServiceDescriptorProto]
    extension: _containers.RepeatedCompositeFieldContainer[FieldDescriptorProto]
    options: FileOptions
    source_code_info: SourceCodeInfo
    syntax: str
    def __init__(self, name: _Optional[str] = ..., package: _Optional[str] = ..., dependency: _Optional[_Iterable[str]] = ..., public_dependency: _Optional[_Iterable[int]] = ..., weak_dependency: _Optional[_Iterable[int]] = ..., message_type: _Optional[_Iterable[_Union[DescriptorProto, _Mapping]]] = ..., enum_type: _Optional[_Iterable[_Union[EnumDescriptorProto, _Mapping]]] = ..., service: _Optional[_Iterable[_Union[ServiceDescriptorProto, _Mapping]]] = ..., extension: _Optional[_Iterable[_Union[FieldDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[FileOptions, _Mapping]] = ..., source_code_info: _Optional[_Union[SourceCodeInfo, _Mapping]] = ..., syntax: _Optional[str] = ...) -> None: ...

class DescriptorProto(_message.Message):
    __slots__ = ("name", "field", "extension", "nested_type", "enum_type", "extension_range", "oneof_decl", "options", "reserved_range", "reserved_name")
    class ExtensionRange(_message.Message):
        __slots__ = ("start", "end", "options")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        options: ExtensionRangeOptions
        def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., options: _Optional[_Union[ExtensionRangeOptions, _Mapping]] = ...) -> None: ...
    class ReservedRange(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    NESTED_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_RANGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_DECL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_RANGE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    field: _containers.RepeatedCompositeFieldContainer[FieldDescriptorProto]
    extension: _containers.RepeatedCompositeFieldContainer[FieldDescriptorProto]
    nested_type: _containers.RepeatedCompositeFieldContainer[DescriptorProto]
    enum_type: _containers.RepeatedCompositeFieldContainer[EnumDescriptorProto]
    extension_range: _containers.RepeatedCompositeFieldContainer[DescriptorProto.ExtensionRange]
    oneof_decl: _containers.RepeatedCompositeFieldContainer[OneofDescriptorProto]
    options: MessageOptions
    reserved_range: _containers.RepeatedCompositeFieldContainer[DescriptorProto.ReservedRange]
    reserved_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., field: _Optional[_Iterable[_Union[FieldDescriptorProto, _Mapping]]] = ..., extension: _Optional[_Iterable[_Union[FieldDescriptorProto, _Mapping]]] = ..., nested_type: _Optional[_Iterable[_Union[DescriptorProto, _Mapping]]] = ..., enum_type: _Optional[_Iterable[_Union[EnumDescriptorProto, _Mapping]]] = ..., extension_range: _Optional[_Iterable[_Union[DescriptorProto.ExtensionRange, _Mapping]]] = ..., oneof_decl: _Optional[_Iterable[_Union[OneofDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[MessageOptions, _Mapping]] = ..., reserved_range: _Optional[_Iterable[_Union[DescriptorProto.ReservedRange, _Mapping]]] = ..., reserved_name: _Optional[_Iterable[str]] = ...) -> None: ...

class ExtensionRangeOptions(_message.Message):
    __slots__ = ("uninterpreted_option",)
    Extensions: _python_message._ExtensionDict
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class FieldDescriptorProto(_message.Message):
    __slots__ = ("name", "number", "label", "type", "type_name", "extendee", "default_value", "oneof_index", "json_name", "options", "proto3_optional")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_DOUBLE: _ClassVar[FieldDescriptorProto.Type]
        TYPE_FLOAT: _ClassVar[FieldDescriptorProto.Type]
        TYPE_INT64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_UINT64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_INT32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_FIXED64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_FIXED32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_BOOL: _ClassVar[FieldDescriptorProto.Type]
        TYPE_STRING: _ClassVar[FieldDescriptorProto.Type]
        TYPE_GROUP: _ClassVar[FieldDescriptorProto.Type]
        TYPE_MESSAGE: _ClassVar[FieldDescriptorProto.Type]
        TYPE_BYTES: _ClassVar[FieldDescriptorProto.Type]
        TYPE_UINT32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_ENUM: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SFIXED32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SFIXED64: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SINT32: _ClassVar[FieldDescriptorProto.Type]
        TYPE_SINT64: _ClassVar[FieldDescriptorProto.Type]
    TYPE_DOUBLE: FieldDescriptorProto.Type
    TYPE_FLOAT: FieldDescriptorProto.Type
    TYPE_INT64: FieldDescriptorProto.Type
    TYPE_UINT64: FieldDescriptorProto.Type
    TYPE_INT32: FieldDescriptorProto.Type
    TYPE_FIXED64: FieldDescriptorProto.Type
    TYPE_FIXED32: FieldDescriptorProto.Type
    TYPE_BOOL: FieldDescriptorProto.Type
    TYPE_STRING: FieldDescriptorProto.Type
    TYPE_GROUP: FieldDescriptorProto.Type
    TYPE_MESSAGE: FieldDescriptorProto.Type
    TYPE_BYTES: FieldDescriptorProto.Type
    TYPE_UINT32: FieldDescriptorProto.Type
    TYPE_ENUM: FieldDescriptorProto.Type
    TYPE_SFIXED32: FieldDescriptorProto.Type
    TYPE_SFIXED64: FieldDescriptorProto.Type
    TYPE_SINT32: FieldDescriptorProto.Type
    TYPE_SINT64: FieldDescriptorProto.Type
    class Label(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LABEL_OPTIONAL: _ClassVar[FieldDescriptorProto.Label]
        LABEL_REQUIRED: _ClassVar[FieldDescriptorProto.Label]
        LABEL_REPEATED: _ClassVar[FieldDescriptorProto.Label]
    LABEL_OPTIONAL: FieldDescriptorProto.Label
    LABEL_REQUIRED: FieldDescriptorProto.Label
    LABEL_REPEATED: FieldDescriptorProto.Label
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENDEE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INDEX_FIELD_NUMBER: _ClassVar[int]
    JSON_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    number: int
    label: FieldDescriptorProto.Label
    type: FieldDescriptorProto.Type
    type_name: str
    extendee: str
    default_value: str
    oneof_index: int
    json_name: str
    options: FieldOptions
    proto3_optional: bool
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ..., label: _Optional[_Union[FieldDescriptorProto.Label, str]] = ..., type: _Optional[_Union[FieldDescriptorProto.Type, str]] = ..., type_name: _Optional[str] = ..., extendee: _Optional[str] = ..., default_value: _Optional[str] = ..., oneof_index: _Optional[int] = ..., json_name: _Optional[str] = ..., options: _Optional[_Union[FieldOptions, _Mapping]] = ..., proto3_optional: bool = ...) -> None: ...

class OneofDescriptorProto(_message.Message):
    __slots__ = ("name", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    options: OneofOptions
    def __init__(self, name: _Optional[str] = ..., options: _Optional[_Union[OneofOptions, _Mapping]] = ...) -> None: ...

class EnumDescriptorProto(_message.Message):
    __slots__ = ("name", "value", "options", "reserved_range", "reserved_name")
    class EnumReservedRange(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_RANGE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[EnumValueDescriptorProto]
    options: EnumOptions
    reserved_range: _containers.RepeatedCompositeFieldContainer[EnumDescriptorProto.EnumReservedRange]
    reserved_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[EnumValueDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[EnumOptions, _Mapping]] = ..., reserved_range: _Optional[_Iterable[_Union[EnumDescriptorProto.EnumReservedRange, _Mapping]]] = ..., reserved_name: _Optional[_Iterable[str]] = ...) -> None: ...

class EnumValueDescriptorProto(_message.Message):
    __slots__ = ("name", "number", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    number: int
    options: EnumValueOptions
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ..., options: _Optional[_Union[EnumValueOptions, _Mapping]] = ...) -> None: ...

class ServiceDescriptorProto(_message.Message):
    __slots__ = ("name", "method", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    method: _containers.RepeatedCompositeFieldContainer[MethodDescriptorProto]
    options: ServiceOptions
    def __init__(self, name: _Optional[str] = ..., method: _Optional[_Iterable[_Union[MethodDescriptorProto, _Mapping]]] = ..., options: _Optional[_Union[ServiceOptions, _Mapping]] = ...) -> None: ...

class MethodDescriptorProto(_message.Message):
    __slots__ = ("name", "input_type", "output_type", "options", "client_streaming", "server_streaming")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STREAMING_FIELD_NUMBER: _ClassVar[int]
    SERVER_STREAMING_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_type: str
    output_type: str
    options: MethodOptions
    client_streaming: bool
    server_streaming: bool
    def __init__(self, name: _Optional[str] = ..., input_type: _Optional[str] = ..., output_type: _Optional[str] = ..., options: _Optional[_Union[MethodOptions, _Mapping]] = ..., client_streaming: bool = ..., server_streaming: bool = ...) -> None: ...

class FileOptions(_message.Message):
    __slots__ = ("java_package", "java_outer_classname", "java_multiple_files", "java_generate_equals_and_hash", "java_string_check_utf8", "optimize_for", "go_package", "cc_generic_services", "java_generic_services", "py_generic_services", "php_generic_services", "deprecated", "cc_enable_arenas", "objc_class_prefix", "csharp_namespace", "swift_prefix", "php_class_prefix", "php_namespace", "php_metadata_namespace", "ruby_package", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    class OptimizeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEED: _ClassVar[FileOptions.OptimizeMode]
        CODE_SIZE: _ClassVar[FileOptions.OptimizeMode]
        LITE_RUNTIME: _ClassVar[FileOptions.OptimizeMode]
    SPEED: FileOptions.OptimizeMode
    CODE_SIZE: FileOptions.OptimizeMode
    LITE_RUNTIME: FileOptions.OptimizeMode
    JAVA_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    JAVA_OUTER_CLASSNAME_FIELD_NUMBER: _ClassVar[int]
    JAVA_MULTIPLE_FILES_FIELD_NUMBER: _ClassVar[int]
    JAVA_GENERATE_EQUALS_AND_HASH_FIELD_NUMBER: _ClassVar[int]
    JAVA_STRING_CHECK_UTF8_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_FOR_FIELD_NUMBER: _ClassVar[int]
    GO_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CC_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    JAVA_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    PY_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    PHP_GENERIC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    CC_ENABLE_ARENAS_FIELD_NUMBER: _ClassVar[int]
    OBJC_CLASS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CSHARP_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SWIFT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PHP_CLASS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PHP_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PHP_METADATA_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    RUBY_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    java_package: str
    java_outer_classname: str
    java_multiple_files: bool
    java_generate_equals_and_hash: bool
    java_string_check_utf8: bool
    optimize_for: FileOptions.OptimizeMode
    go_package: str
    cc_generic_services: bool
    java_generic_services: bool
    py_generic_services: bool
    php_generic_services: bool
    deprecated: bool
    cc_enable_arenas: bool
    objc_class_prefix: str
    csharp_namespace: str
    swift_prefix: str
    php_class_prefix: str
    php_namespace: str
    php_metadata_namespace: str
    ruby_package: str
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, java_package: _Optional[str] = ..., java_outer_classname: _Optional[str] = ..., java_multiple_files: bool = ..., java_generate_equals_and_hash: bool = ..., java_string_check_utf8: bool = ..., optimize_for: _Optional[_Union[FileOptions.OptimizeMode, str]] = ..., go_package: _Optional[str] = ..., cc_generic_services: bool = ..., java_generic_services: bool = ..., py_generic_services: bool = ..., php_generic_services: bool = ..., deprecated: bool = ..., cc_enable_arenas: bool = ..., objc_class_prefix: _Optional[str] = ..., csharp_namespace: _Optional[str] = ..., swift_prefix: _Optional[str] = ..., php_class_prefix: _Optional[str] = ..., php_namespace: _Optional[str] = ..., php_metadata_namespace: _Optional[str] = ..., ruby_package: _Optional[str] = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class MessageOptions(_message.Message):
    __slots__ = ("message_set_wire_format", "no_standard_descriptor_accessor", "deprecated", "map_entry", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    MESSAGE_SET_WIRE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    NO_STANDARD_DESCRIPTOR_ACCESSOR_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    MAP_ENTRY_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    message_set_wire_format: bool
    no_standard_descriptor_accessor: bool
    deprecated: bool
    map_entry: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, message_set_wire_format: bool = ..., no_standard_descriptor_accessor: bool = ..., deprecated: bool = ..., map_entry: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class FieldOptions(_message.Message):
    __slots__ = ("ctype", "packed", "jstype", "lazy", "unverified_lazy", "deprecated", "weak", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    class CType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRING: _ClassVar[FieldOptions.CType]
        CORD: _ClassVar[FieldOptions.CType]
        STRING_PIECE: _ClassVar[FieldOptions.CType]
    STRING: FieldOptions.CType
    CORD: FieldOptions.CType
    STRING_PIECE: FieldOptions.CType
    class JSType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JS_NORMAL: _ClassVar[FieldOptions.JSType]
        JS_STRING: _ClassVar[FieldOptions.JSType]
        JS_NUMBER: _ClassVar[FieldOptions.JSType]
    JS_NORMAL: FieldOptions.JSType
    JS_STRING: FieldOptions.JSType
    JS_NUMBER: FieldOptions.JSType
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIELD_NUMBER: _ClassVar[int]
    JSTYPE_FIELD_NUMBER: _ClassVar[int]
    LAZY_FIELD_NUMBER: _ClassVar[int]
    UNVERIFIED_LAZY_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    WEAK_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    ctype: FieldOptions.CType
    packed: bool
    jstype: FieldOptions.JSType
    lazy: bool
    unverified_lazy: bool
    deprecated: bool
    weak: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, ctype: _Optional[_Union[FieldOptions.CType, str]] = ..., packed: bool = ..., jstype: _Optional[_Union[FieldOptions.JSType, str]] = ..., lazy: bool = ..., unverified_lazy: bool = ..., deprecated: bool = ..., weak: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class OneofOptions(_message.Message):
    __slots__ = ("uninterpreted_option",)
    Extensions: _python_message._ExtensionDict
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class EnumOptions(_message.Message):
    __slots__ = ("allow_alias", "deprecated", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    ALLOW_ALIAS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    allow_alias: bool
    deprecated: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, allow_alias: bool = ..., deprecated: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class EnumValueOptions(_message.Message):
    __slots__ = ("deprecated", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    deprecated: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, deprecated: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class ServiceOptions(_message.Message):
    __slots__ = ("deprecated", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    deprecated: bool
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, deprecated: bool = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class MethodOptions(_message.Message):
    __slots__ = ("deprecated", "idempotency_level", "uninterpreted_option")
    Extensions: _python_message._ExtensionDict
    class IdempotencyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDEMPOTENCY_UNKNOWN: _ClassVar[MethodOptions.IdempotencyLevel]
        NO_SIDE_EFFECTS: _ClassVar[MethodOptions.IdempotencyLevel]
        IDEMPOTENT: _ClassVar[MethodOptions.IdempotencyLevel]
    IDEMPOTENCY_UNKNOWN: MethodOptions.IdempotencyLevel
    NO_SIDE_EFFECTS: MethodOptions.IdempotencyLevel
    IDEMPOTENT: MethodOptions.IdempotencyLevel
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UNINTERPRETED_OPTION_FIELD_NUMBER: _ClassVar[int]
    deprecated: bool
    idempotency_level: MethodOptions.IdempotencyLevel
    uninterpreted_option: _containers.RepeatedCompositeFieldContainer[UninterpretedOption]
    def __init__(self, deprecated: bool = ..., idempotency_level: _Optional[_Union[MethodOptions.IdempotencyLevel, str]] = ..., uninterpreted_option: _Optional[_Iterable[_Union[UninterpretedOption, _Mapping]]] = ...) -> None: ...

class UninterpretedOption(_message.Message):
    __slots__ = ("name", "identifier_value", "positive_int_value", "negative_int_value", "double_value", "string_value", "aggregate_value")
    class NamePart(_message.Message):
        __slots__ = ("name_part", "is_extension")
        NAME_PART_FIELD_NUMBER: _ClassVar[int]
        IS_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        name_part: str
        is_extension: bool
        def __init__(self, name_part: _Optional[str] = ..., is_extension: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_VALUE_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedCompositeFieldContainer[UninterpretedOption.NamePart]
    identifier_value: str
    positive_int_value: int
    negative_int_value: int
    double_value: float
    string_value: bytes
    aggregate_value: str
    def __init__(self, name: _Optional[_Iterable[_Union[UninterpretedOption.NamePart, _Mapping]]] = ..., identifier_value: _Optional[str] = ..., positive_int_value: _Optional[int] = ..., negative_int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[bytes] = ..., aggregate_value: _Optional[str] = ...) -> None: ...

class SourceCodeInfo(_message.Message):
    __slots__ = ("location",)
    class Location(_message.Message):
        __slots__ = ("path", "span", "leading_comments", "trailing_comments", "leading_detached_comments")
        PATH_FIELD_NUMBER: _ClassVar[int]
        SPAN_FIELD_NUMBER: _ClassVar[int]
        LEADING_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        TRAILING_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        LEADING_DETACHED_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedScalarFieldContainer[int]
        span: _containers.RepeatedScalarFieldContainer[int]
        leading_comments: str
        trailing_comments: str
        leading_detached_comments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, path: _Optional[_Iterable[int]] = ..., span: _Optional[_Iterable[int]] = ..., leading_comments: _Optional[str] = ..., trailing_comments: _Optional[str] = ..., leading_detached_comments: _Optional[_Iterable[str]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _containers.RepeatedCompositeFieldContainer[SourceCodeInfo.Location]
    def __init__(self, location: _Optional[_Iterable[_Union[SourceCodeInfo.Location, _Mapping]]] = ...) -> None: ...

class GeneratedCodeInfo(_message.Message):
    __slots__ = ("annotation",)
    class Annotation(_message.Message):
        __slots__ = ("path", "source_file", "begin", "end")
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FILE_FIELD_NUMBER: _ClassVar[int]
        BEGIN_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedScalarFieldContainer[int]
        source_file: str
        begin: int
        end: int
        def __init__(self, path: _Optional[_Iterable[int]] = ..., source_file: _Optional[str] = ..., begin: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    annotation: _containers.RepeatedCompositeFieldContainer[GeneratedCodeInfo.Annotation]
    def __init__(self, annotation: _Optional[_Iterable[_Union[GeneratedCodeInfo.Annotation, _Mapping]]] = ...) -> None: ...
