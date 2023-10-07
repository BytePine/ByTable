import os


class LoadBase:
    path: str
    suffix: str
    skip_start: [str]

    def __init__(self, path: str):
        self.path = path
        self.skip_start = ["~$"]
        self.suffix = ""

    def do_load(self):
        pass

    def find_files(self):
        if self.suffix == "":
            return []
        table_files = []
        for file_path, _, file_names in os.walk(self.path):
            for file_name in file_names:
                skip = False
                for skip_start in self.skip_start:
                    if file_name.startswith(skip_start):
                        skip = True
                        break
                if not file_name.endswith(self.suffix):
                    skip = True
                if skip:
                    continue
                table_files.append(os.path.join(file_path, file_name))
        return table_files
