from .base import Data, Value, DataKind


class Config(Data):
    _elements: dict[str, Value]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = DataKind.Config
        self._elements = dict()

    def __str__(self):
        data_str = super().__str__()
        return f"{data_str} elements:{len(self._elements)}"

    def set_elements(self, elements: dict[str, Value]):
        self._elements = elements

    @property
    def elements(self):
        return self._elements
