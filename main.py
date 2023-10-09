import re

from engine import Engine, EngineConfig
from excel_proto.excel import ExcelFile

engine_config = EngineConfig()
engine_config.load_path = "res/excel"
engine_config.load_suffix = ".xlsx"
engine_config.load_skip = r'~\$(.*)'
engine_config.load_cls = ExcelFile

if __name__ == "__main__":
    engine = Engine()
    engine.run(engine_config)
