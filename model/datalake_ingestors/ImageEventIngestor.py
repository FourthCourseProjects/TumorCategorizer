from abc import ABC

from model.Datalake import Datalake
from model.EventIngestor import EventIngestor
from model.Reader import Reader
from model.Store import Store


class ImageEventIngestor(EventIngestor, ABC):
    def __init__(self, reader: Reader, store: Store):
        self.reader = reader
        self.store = store

    def ingest(self, uri, datalake: Datalake):
        image = self.reader.read(uri)
        self.store.store(datalake, image)
