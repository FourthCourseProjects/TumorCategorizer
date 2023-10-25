import cv2
from model.Dataframe import Dataframe
from model.events.data.Image import Image


class ResizeImageMapper:
    def __init__(self, size):
        self.size = size

    def apply(self, dataframe: Dataframe, column_name, output_column_name):
        dataframe.add(output_column_name, self.process(dataframe.get()[column_name]))

    def process(self, images):
        return [Image(cv2.resize(image.content(), self.size)) for image in images]
