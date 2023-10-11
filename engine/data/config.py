from .base import Data, Value, DataKind


class Config(Data):
    _elements: dict[str, Value]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = DataKind.Config
        self._elements = dict()
