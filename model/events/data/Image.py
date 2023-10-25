from abc import ABC

from model.Data import Data


class Image(Data, ABC):
    def __init__(self, content):
        self._content = content

    def content(self):
        return self._content
