from abc import abstractmethod, ABC


class Data(ABC):
    @abstractmethod
    def content(self):
        pass
