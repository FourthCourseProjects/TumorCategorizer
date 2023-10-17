from abc import ABC, abstractmethod


class SourceHandler(ABC):
    @abstractmethod
    def build_from(self, directory):
        pass

    @abstractmethod
    def add_from(self, directory):
        pass
