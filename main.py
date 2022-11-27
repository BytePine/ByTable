import logging

from src.load import Load
from src.load.param import LoadParam

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(message)s')

if __name__ == '__main__':
    # 加载资源
    Load(LoadParam())
