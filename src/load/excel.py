from ..base import Execute


class LoadExcel(Execute):
    def __init__(self, path):
        super(LoadExcel, self).__init__()
        self.path = path

    def execute(self):
        self.logger.debug(f'LoadExcel:{self.path}')
