import os
from abc import ABC

from model.DatamartBuilder import DatamartBuilder


class ImageFileSystemDatamartBuilder(DatamartBuilder, ABC):
    def __init__(self, data_reader, metadata_reader, datalake_querier, data_writer, datalake):
        self.data_reader = data_reader
        self.metadata_reader = metadata_reader
        self.querier = datalake_querier
        self.data_writer = data_writer
        self.datalake = datalake

    def build(self, datamart_path, categories):
        self._create_directories(datamart_path, categories)
        for category in categories:
            self.writeImages(datamart_path, category, self.uris(category))

    def uris(self, category):
        return list(map(lambda x: self.datalake.directory + "/" + x.uri, self.metadatas(category)))

    def _create_directories(self, root, sub_directories):
        os.makedirs(root)
        for directory in sub_directories: os.makedirs(root + "/" + directory)

    def metadatas(self, category):
        return [self.metadata_reader.read(self.datalake.metadata_tank().directory + "/" + image_metadata)
                for image_metadata in self.querier.query(category)]

    def writeImages(self, root, category, uris):
        for uri in uris:
            self.data_writer.write(root + "/" + category + "/" + uri.split("/")[-1], self.data_reader.read(uri).content())
