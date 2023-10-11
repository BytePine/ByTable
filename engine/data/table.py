from .base import Value, Data, DataKind


class TableRow:
    elements: dict[str, Value]

    def __init__(self):
        self.elements = dict()

    def set_value(self, value: Value):
        self.elements[value.head.key] = value


class Table(Data):
    rows: list[TableRow]

    def __init__(self, name: str):
        super().__init__(name)
        self.kind = DataKind.Table
        self.rows = list()

    def __str__(self):
        data_str = super().__str__()
        return f"{data_str} rows:{len(self.rows)}"
    