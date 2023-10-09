from . import singleton
from .data import DataManager


class LoadFile:
    path: str

    def __init__(self, path: str):
        self.path = path

    def on_load(self) -> []:
        pass


@singleton
class LoadManager:
    load_files: list[LoadFile]
    data_manager: DataManager

    def __init__(self):
        self.load_files = list()
        self.data_manager = DataManager()

    def push_file(self, load_file: LoadFile):
        self.load_files.append(load_file)

    def load_all(self):
        for load_file in self.load_files:
            data_list = load_file.on_load()
            self.data_manager.push_list(data_list)
