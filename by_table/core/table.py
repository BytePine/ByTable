from value import Value


class Row:
    meta: dict[str, Value]

    def __init__(self):
        self.meta = dict()


class Table:
    meta: list[Value]

    def __init__(self):
        self.meta = list()
