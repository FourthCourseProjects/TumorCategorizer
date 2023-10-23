from abc import ABC

from model.Datalake import Datalake
from model.Serializer import Serializer
from model.Store import Store
from model.writers.EventWriter import EventWriter


class EventStore(Store, ABC):
    def __init__(self, event_writer: EventWriter, metadata_serializer: Serializer, data_serializer: Serializer):
        self.writer = event_writer
        self.metadata_serializer = metadata_serializer
        self.data_serializer = data_serializer

    def store(self, datalake: Datalake, event):
        self.writer.write_metadata(self._metadata_file_name(datalake, event), self.metadata_serializer.serialize(event.category()))
        self.writer.write_data(self._data_filename(datalake, event), self.data_serializer.serialize(event.data()))

    def _data_filename(self, datalake, event):
        return datalake.directory + "/" + str(event.category().id) + ".jpg"

    def _metadata_file_name(self, datalake, event):
        return datalake.directory + "/metadata/" + str(event.category().id) + ".metadata"
