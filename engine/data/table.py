from . import Data, Value


class TableRow:
    id: int
    elements: dict[str, Value]

    def __contains__(self, item):
        return self.id == item.id


class Table(Data):
    rows: list[TableRow]
