from . import Data, Value


class Config(Data):
    elements: dict[str, Value]
