import os
import re

from .load import LoadManager


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
            return _instance[cls]

    return inner


def find_files(path: str, suffix: str, skip: str):
    files = []
    if suffix == "":
        return files
    for file_path, _, file_names in os.walk(path):
        for file_name in file_names:
            if (file_name.endswith(suffix) and
                    re.match(skip, file_name) is None):
                files.append(os.path.abspath(os.path.join(file_path, file_name)))
    return files


class EngineConfig:
    load_path: str
    load_suffix: str
    load_skip: str
    load_cls: None
    out_path: str
    out_cls: None


@singleton
class Engine:
    config: EngineConfig
    load_manager: LoadManager

    def __init__(self):
        self.load_manager = LoadManager()

    def run(self, config: EngineConfig):
        load_files = find_files(config.load_path, config.load_suffix, config.load_skip)
        self.load_manager.load_all(config.load_cls, load_files)
