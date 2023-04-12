import logging

from excel import load_excel

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(message)s')

if __name__ == '__main__':
    # 加载表格
    load_excel("D:/Dev/ByTable/res/excel")
