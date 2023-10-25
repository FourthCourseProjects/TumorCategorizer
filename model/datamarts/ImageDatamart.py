import os
from abc import ABC
import matplotlib.pyplot as plt
from model.Datamart import Datamart


class ImageDatamart(Datamart, ABC):
    def __init__(self, directory):
        super().__init__(directory)

    def data_for(self, category):
        return os.listdir(self.directory_for(category))

    def directory_for(self, category):
        return self.directory + "/" + category

    def categories(self):
        return os.listdir(self.directory)

    def data_per_category(self):
        return dict(zip(self.categories(), self._number_of_images_per_category()))

    def _number_of_images_per_category(self):
        return [len(self.data_for(category)) for category in self.categories()]