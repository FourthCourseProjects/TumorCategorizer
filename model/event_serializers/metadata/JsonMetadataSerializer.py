import json
from abc import ABC

from model.Metadata import Metadata
from model.Serializer import Serializer


class JsonMetadataSerializer(Serializer, ABC):
    def serialize(self, metadata: Metadata) -> str:
        return json.dumps(metadata.to_dict())
