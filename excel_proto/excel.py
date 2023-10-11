import re

import openpyxl
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

from engine.data import Table, Config, Enumerate
from engine.data.check import Check
from engine.data.table import TableRow
from engine.load import LoadFile
from engine.data.base import string_to_data_kind, DataKind, Head, Value, data_type_to_value_kind


def get_cell(cell: Cell):
    value = cell.value
    if value is None:
        return None
    if cell.data_type != "s":
        return value
    if value.startswith("#"):
        return None
    return value


def to_data(ws: Worksheet):
    info_cell: Cell = ws.cell(1, 1)
    cell_value = get_cell(info_cell)
    if cell_value is None:
        return None
    match = re.match(r"(.*)<(.*)>", cell_value)
    if match and len(match.groups()) != 2:
        return None
    kind = string_to_data_kind(match.group(1))
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

    # Key
    key_dict: dict[int, str] = dict()
    key_row = next(ws.iter_rows(2))
    for cell in key_row:
        cell_str = get_cell(cell)
        if cell_str:
            key_dict[cell.col_idx] = cell_str

    # Desc
    desc_dict: dict[int, str] = dict()
    desc_row = next(ws.iter_rows(3))
    for cell in desc_row:
        if cell.col_idx in key_dict.keys():
            desc_dict[cell.col_idx] = get_cell(cell)

    # Head
    head_dict: dict[int, Head] = dict()
    for key in key_dict.keys():
        head = Head()
        head.key = key_dict.get(key)
        head.desc = desc_dict.get(key)
        head_dict[key] = head

    # Values
    row_list: list[TableRow] = list()
    for value_row in ws.iter_rows(4):
        table_row = TableRow()
        row_list.append(table_row)
        for cell in value_row:
            if cell.col_idx in head_dict.keys():
                value = Value()
                value.head = head_dict[cell.col_idx]
                value.meta = get_cell(cell)
                value.kind = data_type_to_value_kind(cell.data_type)
                table_row.set_value(value)

    table.rows = row_list
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
                print(data)
                yield data
