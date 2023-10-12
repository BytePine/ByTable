from enum import Enum


# 数据类型
class ValueKind(Enum):
    Null = 0
    Number = 1
    String = 2
    DateTime = 3
    Array = 4
    Struct = 5


# 数据
class Value:
    _meta = None
    _kind: ValueKind

    def __init__(self, kind: ValueKind, value):
        self._kind = kind
        self._meta = value

    @property
    def meta(self):
        return self._meta


# 页签类型
class PageKind(Enum):
    Null = 0
    Table = 1
    Config = 2
    Enum = 3


# 页签
class Page:
    _name: str
    _kind: PageKind

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind


# 表格行
class TableRow:
    _elements: dict[str, Value]

    def __init__(self):
        self._elements = dict()

    def set_value(self, key: str, value: Value):
        self._elements[key] = value

    @property
    def elements(self):
        return self._elements

    def value(self, key: str):
        return self._elements.get(key)


# 表格链接
class TableLink:
    _table_name: str
    _key: str

    def __init__(self, table_name: str, key: str):
        self._table_name = table_name
        self._key = key

    def table_name(self):
        return self._table_name

    def key(self):
        return self._key


# 表格页签
class TablePage(Page):
    _elements: list[TableRow]
    _links: list[TableLink]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = PageKind.Table
        self._elements = list()
        self._links = list()

    def append_element(self, element: TableRow):
        self._elements.append(element)

    def append_link(self, link: TableLink):
        self._links.append(link)

    @property
    def elements(self):
        return self._elements

    def cols(self, key: str):
        cols: list[Value] = list()
        for element in self._elements:
            cols.append(element.value(key))
        return cols


# 枚举行
class EnumRow:
    _value: int
    _text: str
    _desc: str

    def __init__(self, value: int, text: str, desc: str):
        self._value = value
        self._desc = desc
        self._text = text

    @property
    def value(self):
        return self._value

    @property
    def desc(self):
        return self._desc

    @property
    def text(self):
        return self.text()


# 枚举页签
class EnumPage(Page):
    _elements: dict[str, EnumRow]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = PageKind.Enum
        self._elements = dict()

    def set_element(self, key: str, value: EnumRow):
        self._elements[key] = value

    @property
    def elements(self):
        return self._elements


# 配置页签
class ConfigPage(Page):
    _elements: dict[str, Value]

    def __init__(self, name: str):
        super().__init__(name)
        self._kind = PageKind.Config
        self._elements = dict()

    def set_element(self, key: str, value: Value):
        self._elements[key] = value

    @property
    def elements(self):
        return self._elements


# 数据管理
class DataManager:
    tables: dict[str, list[TablePage]]
    configs: dict[str, list[ConfigPage]]
    enumerates: dict[str, list[EnumPage]]

    def __init__(self):
        self.tables = dict()
        self.configs = dict()
        self.enumerates = dict()

    def push_list(self, data_list: list[Page]):
        for data in data_list:
            if data.kind == PageKind.Table:
                self.push_table(data)
            elif data.kind == PageKind.Config:
                self.push_config(data)
            elif data.kind == PageKind.Enum:
                self.push_enumerate(data)

    def push_table(self, data):
        name = data.name
        table_list = self.tables.get(name)
        if table_list is None:
            table_list = list()
            self.tables[name] = table_list
        table_list.append(data)

    def push_config(self, data):
        name = data.name
        config_list = self.configs.get(name)
        if config_list is None:
            config_list = list()
            self.configs[name] = config_list
        config_list.append(data)

    def push_enumerate(self, data):
        name = data.name
        enumerate_list = self.enumerates.get(name)
        if enumerate_list is None:
            enumerate_list = list()
            self.enumerates[name] = enumerate_list
        enumerate_list.append(data)
