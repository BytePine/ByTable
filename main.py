from engine import Engine, EngineConfig
from laod.excel import ExcelLoad

engine_config = EngineConfig()
engine_config.load_path = "res/excel"
engine_config.load_suffix = ".xlsx"
engine_config.load_skip = r'~\$(.*)'
engine_config.load_cls = ExcelLoad

if __name__ == "__main__":
    engine = Engine()
    engine.run(engine_config)
