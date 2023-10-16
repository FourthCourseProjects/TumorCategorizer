from abc import ABC

from model.DatalakeHandler import DatalakeHandler


class ImageFileSystemStructureDatalakeHandler(DatalakeHandler, ABC):
    def __init__(self) -> None:
        super().__init__()

    def build_from(self, directory):
        pass

    def add_from(self, directory):
        pass
