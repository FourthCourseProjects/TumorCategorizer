from abc import ABC, abstractmethod


class Deserializer(ABC):
    @abstractmethod
    def deserialize(self, string):
        pass
