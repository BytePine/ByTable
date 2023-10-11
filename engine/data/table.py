from .base import Value, Data, DataKind


class TableRow:
    _elements: dict[str, Value]

    def __init__(self):
        self._elements = dict()

    def set_value(self, value: Value):
        self._elements[value.head.key] = value

    @property
    def elements(self):
        return self._elements


class Table(Data):
    _rows: list[TableRow]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = DataKind.Table
        self._rows = list()

    def __str__(self):
        data_str = super().__str__()
        return f"{data_str} rows:{len(self._rows)}"

    def set_rows(self, rows: list[TableRow]):
        self._rows = rows

    @property
    def rows(self):
        return self._rows
