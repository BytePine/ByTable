import logging
import os
import argparse


class Base:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)


class Execute(Base):
    def __init__(self):
        super(Execute, self).__init__()
        self._execute_list = list()

    def push_execute(self, execute):
        self._execute_list.append(execute)

    def pop_execute(self, name):
        for execute in self._execute_list:
            if execute.__class__.__name__ == name:
                self._execute_list.remove(execute)
                break

    def execute(self):
        for execute in self._execute_list:
            execute.execute()


class Env(Base):
    def __init__(self):
        super(Env, self).__init__()

    def get_value(self, name, default=None):
        value = os.getenv(name) or default
        if value is None:
            self.logger.error(f'环境变量：{name} 为空')
            exit(1)
        return value


class Arg(Base):
    def __init__(self):
        super(Arg, self).__init__()
        paser = argparse.ArgumentParser()
        self.reg_argument(paser)
        self.get_argument(paser.parse_args())

    def reg_argument(self, parser: argparse.ArgumentParser):
        pass

    def get_argument(self, args):
        pass
