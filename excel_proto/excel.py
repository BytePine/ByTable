from engine.load import LoadFile


class ExcelFile(LoadFile):
    def __init__(self, path: str):
        super().__init__(path)

    def on_load(self) -> []:
        print(self.path)
        return []
