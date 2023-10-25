import json
from abc import ABC

from model.Deserializer import Deserializer
from model.events.metadata.ImageMetadata import ImageMetadata


class JsonMetadataDeserializer(Deserializer, ABC):
    def deserialize(self, string):
        dic = json.loads(string)
        return ImageMetadata(dic["source"], dic["category"], dic["id"], dic["uri"], dic["ts"])
