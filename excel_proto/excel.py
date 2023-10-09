import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

from engine.load import LoadFile


class ExcelFile(LoadFile):
    def __init__(self, path: str):
        super().__init__(path)

    def on_load(self) -> []:
        print(self.path)
        wb = openpyxl.load_workbook(self.path)
        for ws in wb:
            self.on_worksheet(ws)
        return []

    def on_worksheet(self, ws: Worksheet):
        print(ws)