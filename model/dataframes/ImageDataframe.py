from abc import ABC

import numpy as np
import torch

from model.Dataframe import Dataframe
from model.Datamart import Datamart
from model.Dataset import Dataset
from model.Entry import Entry
from model.dataframe_data.UnloadedImage import UnloadedImage


def custom_range(start, end, step):
    result = list(range(start, end, step))
    if result[-1] != end: result.append(end - 1)
    return result


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

    def __len__(self):
        return len(list(self._dictionary.values())[0])

    def column_names(self):
        return list(self._dictionary.keys())

    def to_dataset(self, input_columns, output_columns, batch_size):
        return Dataset(self._create_entries(input_columns, output_columns, batch_size), batch_size)

    def _create_entries(self, input_column, output_columns, batch_size):
        indexes, entries = custom_range(0, len(self), batch_size), []
        for i in range(len(indexes) - 1):
            entries.append(Entry(torch.tensor(self._create(input_column, indexes[i], indexes[i + 1])),
                                 torch.tensor(self._create_output(output_columns, indexes[i], indexes[i + 1]))))
        return entries

    def _create(self, column, start, finish):
        return np.array([image.content() for image in self._dictionary[column][start:finish]])

    def _create_output(self, columns, start, finish):
        return np.array([self._dictionary[column][start:finish] for column in columns]).transpose()
