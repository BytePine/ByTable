from enum import Enum


class ValueType(Enum):
    Boolean = 0,
    Integer = 1,
    Float = 2,
    String = 3,
    Struct = 4,
    Enum = 5,
    DateTime = 6,
