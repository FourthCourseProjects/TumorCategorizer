from abc import ABC

from model.Reader import Reader


class DatalakeMetadataReader(Reader, ABC):
    def __init__(self, reader, metadata_deserializer):
        self.metadata_deserializer = metadata_deserializer
        self.reader = reader

    def read(self, path):
        return self.metadata_deserializer.deserialize(self.reader.read(path))
