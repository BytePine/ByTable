from value import Value


class Config:
    meta: dict[str, Value]

    def __init__(self):
        self.meta = dict()
