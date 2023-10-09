from .base import Data, DataKind


class Check(Data):

    def __init__(self, name: str):
        super().__init__(name)
        self.kind = DataKind.Check
