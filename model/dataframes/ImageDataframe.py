from abc import ABC

from model.Dataframe import Dataframe
from model.Datamart import Datamart
from model.dataframe_data.UnloadedImage import UnloadedImage


class ImageDataframe(Dataframe, ABC):
    def __init__(self, datamart: Datamart):
        self._dictionary = self._create_dictionary(datamart)

    def _create_dictionary(self, datamart: Datamart):
        tuple_list = []
        for category in datamart.categories():
            tuple_list.extend(zip(datamart.data_for(category), [category] * len(datamart.data_for(category))))
        return {"Input": [UnloadedImage(datamart.directory + "/" + tup[1] + "/" + tup[0]) for tup in tuple_list],
                "Output": [tup[1] for tup in tuple_list]}

    def load_images(self):
        self._dictionary["Input"] = [unloaded_image.load() for unloaded_image in self._dictionary["Input"]]

    def get(self):
        return self._dictionary

    def add(self, column_name, values):
        self._dictionary[column_name] = values

    def column_names(self):
        return list(self._dictionary.keys())
