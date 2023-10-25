from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def store(self, path, data):
        pass
