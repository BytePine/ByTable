import os
from enum import Enum


class KindEnum(Enum):
    Error = -1
    Null = 0
    Table = 1
    Config = 2
    Enum = 3
    Check = 4


def str_to_kind(kind: str):
    for kind_enum in KindEnum:
        if kind_enum.name == kind:
            return kind_enum
    return KindEnum.Error


def find_files(path: str, suffix: str, skip_start: [str]):
    if suffix == "":
        return []
    table_files = []
    for file_path, _, file_names in os.walk(path):
        for file_name in file_names:
            skip = False
            for start in skip_start:
                if file_name.startswith(start):
                    skip = True
                    break
            if not file_name.endswith(suffix):
                skip = True
            if skip:
                continue
            table_files.append(os.path.join(file_path, file_name))
    return table_files


class SetInfo:
    _kind: KindEnum
    _name: str

    def __init__(self):
        self._kind = KindEnum.Null
        self._name = ""

    def init_value(self, kind: str, name: str):
        self._name = name
        self._kind = str_to_kind(kind)

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    def __str__(self):
        return f"{self.__class__.__name__}: {self._kind.name}<{self._name}>"
