import os

from model.DatalakeHandler import SourceHandler


class ImageFileSystemStructureDatalakeHandler(SourceHandler):
    def __init__(self, datalake_root: str, writer):
        self.datalake_root = datalake_root
        self.writer = writer

    def build_from(self, directory):
        self._create_directory(self.datalake_root)
        self._create_directory(self.datalake_root + "/metadata")
        self.add_from(directory)

    def add_from(self, directory):
        pass

    def _create_directory(self, path):
        os.makedirs(path)
