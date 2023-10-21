from abc import ABC
import cv2
from model.Writer import Writer


class ImageDataWriter(Writer, ABC):
    def write(self, path, data):
        cv2.imwrite(path, data)
