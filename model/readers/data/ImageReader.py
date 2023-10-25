from abc import ABC

import cv2

from model.Reader import Reader
from model.events.data.Image import Image


class ImageReader(Reader, ABC):
    def read(self, path):
        return Image(cv2.imread(path))
