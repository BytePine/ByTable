from .base import Data, Value, DataKind


class Config(Data):
    elements: dict[str, Value]

    def __init__(self, name: str):
        super().__init__(name)
        self.kind = DataKind.Config
        self.elements = dict()
