from . import Data


class EnumerateRow:
    key: str
    value: int
    text: str
    desc: str


class Enumerate(Data):
    rows: list[EnumerateRow]
