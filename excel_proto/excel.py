import re

import openpyxl
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

from engine.data import Table, Config, Enumerate
from engine.data.check import Check
from engine.load import LoadFile
from engine.data.base import string_to_kind, DataKind


def to_data(ws: Worksheet):
    info_cell: Cell = ws.cell(1, 1)
    cell_value = info_cell.value
    if cell_value is None:
        return None
    match = re.match(r"(.*)<(.*)>", cell_value)
    if match and len(match.groups()) != 2:
        return None
    kind = string_to_kind(match.group(1))
    name = match.group(2)
    if kind == DataKind.Table:
        return to_table(name, ws)
    elif kind == DataKind.Config:
        return to_config(name, ws)
    elif kind == DataKind.Enum:
        return to_enumerate(name, ws)
    elif kind == DataKind.Check:
        return to_check(name, ws)
    return None


def to_table(name: str, ws: Worksheet):
    table = Table(name)
    return table


def to_config(name: str, ws: Worksheet):
    config = Config(name)
    return config


def to_enumerate(name: str, ws: Worksheet):
    enum = Enumerate(name)
    return enum


def to_check(name: str, ws: Worksheet):
    check = Check(name)
    return check


class ExcelFile(LoadFile):
    def __init__(self, path: str):
        super().__init__(path)

    def on_load(self) -> []:
        print(self.path)
        wb = openpyxl.load_workbook(self.path)
        for ws in wb:
            data = to_data(ws)
            if data is not None:
                print(data.name, data.kind)
                yield data
