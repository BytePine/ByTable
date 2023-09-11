from type import ValueType


class Value:
    meta: str
    value_type: ValueType

    def __init__(self, meta: str, value_type: ValueType):
        self.meta = meta
        self.value_type = value_type
