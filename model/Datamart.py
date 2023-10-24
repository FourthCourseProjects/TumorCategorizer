from abc import ABC, abstractmethod


class Datamart(ABC):
    def __init__(self, directory):
        self.directory = directory

    @abstractmethod
    def data_for(self, category):
        pass

    @abstractmethod
    def directory_for(self, category):
        pass

    @abstractmethod
    def categories(self):
        pass

    @abstractmethod
    def data_per_category(self):
        pass
