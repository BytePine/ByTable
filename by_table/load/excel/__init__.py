import openpyxl

from .sheet import Sheet
from ...core import SetInfo, find_files

skip_start = ["~$"]
suffix = ".xlsx"


class DataBase:
    _head: SetInfo


def load(path: str):
    sheets: [Sheet] = []
    files = find_files(path, suffix, skip_start)
    for file in files:
        wb = openpyxl.load_workbook(file)
        for ws in wb:
            sheets.append(Sheet(ws))

