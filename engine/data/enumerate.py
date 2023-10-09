from . import Data, DataKind


class EnumerateRow:
    key: str
    value: int
    text: str
    desc: str


class Enumerate(Data):
    rows: list[EnumerateRow]

    def __init__(self, name: str):
        super().__init__(name)
        self.kind = DataKind.Enum
        self.rows = list()