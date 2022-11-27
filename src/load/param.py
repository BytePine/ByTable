import argparse

from ..base import Arg


class LoadParam(Arg):
    def __init__(self):
        self.excel_path = str()
        self.proto_path = str()
        super(LoadParam, self).__init__()

    def reg_argument(self, parser: argparse.ArgumentParser):
        parser.add_argument('excel_path', type=str)
        parser.add_argument('proto_path', type=str)

    def get_argument(self, args):
        self.excel_path = args.excel_path
        self.proto_path = args.proto_path
