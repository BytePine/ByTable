from enum import Enum


class DataKind(Enum):
    Error = 0
    Table = 1
    Config = 2
    Enumerate = 3
    Check = 4


class ValueKind(Enum):
    Null = 0
    Number = 1
    String = 2


class Data:
    name: str
    kind: DataKind


class Value:
    meta: None
    kind: ValueKind
