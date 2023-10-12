from . import Data, DataKind


class EnumerateRow:
    _key: str
    _value: int
    _text: str
    _desc: str

    def __init__(self, key: str):
        self._key = key

    def set_value(self, value: int):
        self._value = value

    def set_text(self, text: str):
        self._text = text

    def set_desc(self, desc: str):
        self._desc = desc

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def text(self):
        return self._text

    @property
    def desc(self):
        return self._desc


class Enumerate(Data):
    _elements: dict[str, EnumerateRow]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = DataKind.Enum
        self._elements = dict()

    def set_elements(self, elements: dict[str, EnumerateRow]):
        self._elements = elements

    @property
    def elements(self):
        return self._elements

    def __str__(self):
        data_str = super().__str__()
        return f"{data_str} elements:{len(self._elements)}"
