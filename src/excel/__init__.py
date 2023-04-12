class Excel:
    file: str

    def __init__(self, file: str):
        self.file = file
        


def load_excel(path: str):
    print(path)
