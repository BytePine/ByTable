from enum import Enum


class DataKind(Enum):
    Error = 0
    Table = 1
    Config = 2
    Enum = 3
    Check = 4


def string_to_data_kind(kind: str):
    for kind_enum in DataKind:
        if kind_enum.name == kind:
            return kind_enum
    return DataKind.Error


class ValueKind(Enum):
    Null = 0
    Number = 1
    String = 2
    DateTime = 4


def data_type_to_value_kind(data_type: str):
    if data_type == 's':
        return ValueKind.String
    elif data_type == 'n':
        return ValueKind.Number
    elif data_type == 'd':
        return ValueKind.DateTime
    return ValueKind.Null


class Data:
    name: str
    kind: DataKind

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.kind.name}<{self.name}>"


class Head:
    key: str
    desc: str

    def __str__(self):
        return f"{self.key}({self.desc})"


class Value:
    head: Head
    meta: None
    kind: ValueKind

    def __str__(self):
        return f"{self.head} {self.meta}:{self.kind}"
