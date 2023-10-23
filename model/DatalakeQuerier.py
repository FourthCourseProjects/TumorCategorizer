import os

from model.Datalake import Datalake


class DatalakeQuerier:
    def __init__(self, reader, datalake: Datalake):
        self.reader = reader
        self._datalake = datalake

    def query(self, category):
        print("")
        return list(filter(lambda file_name: self.category(file_name) == category, os.listdir(self.metadata_directory())))

    def metadata_directory(self):
        return self._datalake.metadata_tank().directory

    def category(self, file_name):
        return self.reader.read(self.path(file_name)).category

    def path(self, x):
        return self.metadata_directory() + "/" + x
