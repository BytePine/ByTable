import logging

from src.load import Load
from src.load.param import LoadParam

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(message)s')

if __name__ == '__main__':
    # 加载参数
    load_param = LoadParam()
    # 加载资源
    Load(load_param)
