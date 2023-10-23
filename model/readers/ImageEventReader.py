from abc import ABC
from model.Reader import Reader
import cv2

from model.events.ImageEvent import ImageEvent
from model.events.data.Image import Image
from model.events.metadata.ImageMetadata import ImageMetadata


class ImageEventReader(Reader, ABC):
    def read(self, path):
        return ImageEvent(Image(cv2.imread(path)), self._metadata(path))

    def _metadata(self, path):
        return ImageMetadata.init_from(path, self._category(path))

    def _category(self, path):
        return path.split("/")[-2]
