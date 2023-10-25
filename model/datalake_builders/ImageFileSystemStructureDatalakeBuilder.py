import os
from abc import ABC

from model.DatalakeBuilder import DatalakeBuilder
from model.EventIngestor import EventIngestor


class ImageFileSystemStructureDatalakeBuilder(DatalakeBuilder, ABC):
    def __init__(self, datalake, image_ingestor: EventIngestor):
        self.datalake = datalake
        self.image_ingestor = image_ingestor

    def _build(self):
        self._create_directory(self.datalake.directory)
        self._create_directory(self.datalake.directory + "/metadata")

    def add_from(self, directory):
        if not self._datalake_exists(): self._build()
        for category in os.listdir(directory):
            self.images_from(self._append_directories(directory, category))

    def _datalake_exists(self):
        return os.path.exists(self.datalake.directory)

    def _append_directories(self, father, directory):
        return father + "/" + directory

    def _create_directory(self, path):
        os.makedirs(path)

    def images_from(self, category_directory):
        for image in os.listdir(category_directory):
            self.image_ingestor.ingest(self._append_directories(category_directory, image), self.datalake)
