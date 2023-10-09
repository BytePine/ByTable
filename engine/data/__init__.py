from .base import Data, DataKind
from .table import Table
from .config import Config
from .enumerate import Enumerate


class DataManager:
    tables: dict[str, list[Table]]
    configs: dict[str, list[Config]]
    enumerates: dict[str, list[Enumerate]]

    def __init__(self):
        self.tables = dict()
        self.configs = dict()
        self.enumerates = dict()

    def push_list(self, data_list: list[Data]):
        for data in data_list:
            if data.kind == DataKind.Table:
                self.push_table(data)
            elif data.kind == DataKind.Config:
                self.push_config(data)
            elif data.kind == DataKind.Enum:
                self.push_enumerate(data)

    def push_table(self, data):
        name = data.name
        table_list = self.tables.get(name)
        if table_list is None:
            table_list = list()
            self.tables[name] = table_list
        table_list.append(data)

    def push_config(self, data):
        name = data.name
        config_list = self.configs.get(name)
        if config_list is None:
            config_list = list()
            self.configs[name] = config_list
        config_list.append(data)

    def push_enumerate(self, data):
        name = data.name
        enumerate_list = self.enumerates.get(name)
        if enumerate_list is None:
            enumerate_list = list()
            self.enumerates[name] = enumerate_list
        enumerate_list.append(data)
