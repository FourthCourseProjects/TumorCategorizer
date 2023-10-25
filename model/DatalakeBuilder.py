from abc import ABC, abstractmethod


class DatalakeBuilder(ABC):
    @abstractmethod
    def _build(self):
        pass

    @abstractmethod
    def add_from(self, directory):
        pass
