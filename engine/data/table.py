from .base import Value, Data, DataKind


class TableRow:
    id: int
    elements: dict[str, Value]

    def __init__(self):
        self.elements = dict()

    def __contains__(self, item):
        return self.id == item.id


class Table(Data):
    rows: list[TableRow]

    def __init__(self, name: str):
        super().__init__(name)
        self.kind = DataKind.Table
        self.rows = list()
