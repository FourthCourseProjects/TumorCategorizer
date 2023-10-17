import json
from model.data_types.Image import Image


class ImageJsonSerializer:
    def serialize(self, image: Image):
        print(json.dumps(image.to_dict()))
