import uuid
from abc import ABC
from datetime import datetime

from model.Metadata import Metadata


class ImageMetadata(Metadata, ABC):
    def __init__(self, source, category):
        self.source = source
        self.category = category
        self.id = uuid.uuid1()
        self.uri = self.id.__str__() + ".jpg"
        self.ts = datetime.now()

    def to_dict(self) -> dict:
        return {'id': self.id.__str__(),
                'ts': str(self.ts),
                'type': "image",
                'source': self.source,
                'category': self.category,
                'uri': self.uri}
