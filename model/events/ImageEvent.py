from abc import ABC

from model.Event import Event
from model.events.data.Image import Image
from model.events.metadata.ImageMetadata import ImageMetadata


class ImageEvent(Event, ABC):
    def __init__(self, image: Image, image_metadata: ImageMetadata):
        self._image = image
        self._image_metadata = image_metadata

    def data(self):
        return self._image

    def metadata(self):
        return self._image_metadata
