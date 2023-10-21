from abc import ABC, abstractmethod


class EventIngestor(ABC):
    @abstractmethod
    def ingest(self, uri, datalake):
        pass
