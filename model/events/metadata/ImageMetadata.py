import uuid
from abc import ABC
from datetime import datetime

from model.Metadata import Metadata


class ImageMetadata(Metadata, ABC):
    def __init__(self, source, category, id, uri, ts):
        self.source = source
        self.category = category
        self.id = id
        self.uri = uri
        self.ts = ts

    @staticmethod
    def init_from(source, category):
        id = uuid.uuid1()
        return ImageMetadata(source, category, id, id.__str__() + ".jpg", datetime.now())

    def to_dict(self) -> dict:
        return {'id': self.id.__str__(),
                'ts': str(self.ts),
                'type': "image",
                'source': self.source,
                'category': self.category,
                'uri': self.uri}
