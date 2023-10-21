from model.Writer import Writer


class EventWriter:
    def __init__(self, data_writer: Writer, metadata_writer: Writer):
        self._data_writer = data_writer
        self._metadata_writer = metadata_writer

    def write_data(self, path, data_serializer):
        self._data_writer.write(path, data_serializer)

    def write_metadata(self, path, metadata_serialized):
        self._metadata_writer.write(path, metadata_serialized)
