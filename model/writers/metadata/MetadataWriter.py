from abc import ABC
from model.Writer import Writer


class MetadataWriter(Writer, ABC):
    def write(self, path, data):
        with open(path, "w") as file:
            file.write(data)
