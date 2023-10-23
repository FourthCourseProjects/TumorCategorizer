from abc import ABC, abstractmethod


class Reader(ABC):
    def read(self, path):
        with open(path) as f:
            return f.read()
