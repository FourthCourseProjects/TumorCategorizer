from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def data(self):
        pass

    @abstractmethod
    def metadata(self):
        pass
