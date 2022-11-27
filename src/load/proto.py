from ..base import Execute


class LoadProto(Execute):
    def __init__(self, path):
        super(LoadProto, self).__init__()
        self.path = path

    def execute(self):
        self.logger.debug(f'LoadProto:{self.path}')
