from model.readers.data.ImageReader import ImageReader


class UnloadedImage:
    def __init__(self, path):
        self.path = path

    def load(self):
        return ImageReader().read(self.path)
