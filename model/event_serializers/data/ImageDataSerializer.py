from abc import ABC

from model.Data import Data
from model.Serializer import Serializer


class ImageDataSerializer(Serializer, ABC):
    def serialize(self, data: Data) -> str:
        return data.content()
