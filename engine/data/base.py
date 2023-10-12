from enum import Enum


class DataKind(Enum):
    Error = 0
    Table = 1
    Config = 2
    Enum = 3


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
    _name: str
    _kind: DataKind

    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return f"{self._kind.name}<{self._name}>"

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind


class Head:
    _idx: int
    _key: str
    _desc: str

    def __init__(self, idx: int):
        self._idx = idx

    def __str__(self):
        return f"{self._key}({self._desc})"

    def set_key(self, key: str):
        self._key = key

    def set_desc(self, desc: str):
        self._desc = desc

    @property
    def idx(self):
        return self._idx

    @property
    def key(self):
        return self._key

    @property
    def desc(self):
        return self._desc


class Value:
    _head: Head
    _meta: None
    _kind: ValueKind

    def __init__(self, head: Head):
        self._head = head
        self._kind = ValueKind.Null

    def __str__(self):
        return f"{self._head} {self._meta}:{self._kind}"

    def set_meta(self, meta):
        self._meta = meta

    def set_kind(self, kind: ValueKind):
        self._kind = kind

    @property
    def head(self):
        return self._head

    @property
    def meta(self):
        return self._meta

    @property
    def kind(self):
        return self._kind
