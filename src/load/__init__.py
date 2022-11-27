from .excel import LoadExcel
from .param import LoadParam
from .proto import LoadProto
from ..base import Execute


class Load(Execute):
    def __init__(self, load_param: LoadParam):
        super(Load, self).__init__()
        self.push_execute(LoadExcel(load_param.excel_path))
        self.push_execute(LoadProto(load_param.proto_path))
        self.execute()
