import re

from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet
from ...core import SetInfo


def get_info(ws: Worksheet):
    info = SetInfo()
    info_cell: Cell = ws.cell(1, 1)
    if info_cell.value:
        match = re.match(r'(.*)<(.*)>', info_cell.value)
        if len(match.groups()) == 2:
            info.init_value(match.group(1), match.group(2))
    return info


class Sheet:
    _ws: Worksheet
    _info: SetInfo

    def __init__(self, ws: Worksheet):
        self._ws = ws
        self._info = get_info(ws)
        print(self._info)
