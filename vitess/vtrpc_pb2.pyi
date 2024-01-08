from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[Code]
    CANCELED: _ClassVar[Code]
    UNKNOWN: _ClassVar[Code]
    INVALID_ARGUMENT: _ClassVar[Code]
    DEADLINE_EXCEEDED: _ClassVar[Code]
    NOT_FOUND: _ClassVar[Code]
    ALREADY_EXISTS: _ClassVar[Code]
    PERMISSION_DENIED: _ClassVar[Code]
    RESOURCE_EXHAUSTED: _ClassVar[Code]
    FAILED_PRECONDITION: _ClassVar[Code]
    ABORTED: _ClassVar[Code]
    OUT_OF_RANGE: _ClassVar[Code]
    UNIMPLEMENTED: _ClassVar[Code]
    INTERNAL: _ClassVar[Code]
    UNAVAILABLE: _ClassVar[Code]
    DATA_LOSS: _ClassVar[Code]
    UNAUTHENTICATED: _ClassVar[Code]
    CLUSTER_EVENT: _ClassVar[Code]
    READ_ONLY: _ClassVar[Code]
OK: Code
CANCELED: Code
UNKNOWN: Code
INVALID_ARGUMENT: Code
DEADLINE_EXCEEDED: Code
NOT_FOUND: Code
ALREADY_EXISTS: Code
PERMISSION_DENIED: Code
RESOURCE_EXHAUSTED: Code
FAILED_PRECONDITION: Code
ABORTED: Code
OUT_OF_RANGE: Code
UNIMPLEMENTED: Code
INTERNAL: Code
UNAVAILABLE: Code
DATA_LOSS: Code
UNAUTHENTICATED: Code
CLUSTER_EVENT: Code
READ_ONLY: Code

class CallerID(_message.Message):
    __slots__ = ("principal", "component", "subcomponent")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SUBCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    principal: str
    component: str
    subcomponent: str
    def __init__(self, principal: _Optional[str] = ..., component: _Optional[str] = ..., subcomponent: _Optional[str] = ...) -> None: ...

class RPCError(_message.Message):
    __slots__ = ("message", "code")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    code: Code
    def __init__(self, message: _Optional[str] = ..., code: _Optional[_Union[Code, str]] = ...) -> None: ...
