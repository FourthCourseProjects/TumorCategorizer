from abc import ABC, abstractmethod


class Dataframe(ABC):
    @abstractmethod
    def get(self):
        pass

    def add(self, column_name, values):
        pass

    @abstractmethod
    def column_names(self):
        pass

