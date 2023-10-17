import uuid


class Image:
    def __init__(self, source, category, id_=uuid.uuid1()):
        self.source = source
        self.category = category
        self.id = id_

    def to_dict(self):
        return {'source': self.source,
                'category': self.category,
                'id': self.id.__str__(),
                'type': "image"}
