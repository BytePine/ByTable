from enum import Enum


class DataKind(Enum):
    Error = 0
    Table = 1
    Config = 2
    Enum = 3
    Check = 4


def string_to_kind(kind: str):
    for kind_enum in DataKind:
        if kind_enum.name == kind:
            return kind_enum
    return DataKind.Error


class ValueKind(Enum):
    Null = 0
    Number = 1
    String = 2


class Data:
    name: str
    kind: DataKind

    def __init__(self, name: str):
        self.name = name


class Value:
    meta: None
    kind: ValueKind
