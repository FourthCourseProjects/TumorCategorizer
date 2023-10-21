from model.Datalake import Datalake
from model.datalake_builders.ImageFileSystemStructureDatalakeHandler import ImageFileSystemStructureDatalakeHandler
from model.datalake_ingestors.ImageEventIngestor import ImageEventIngestor
from model.event_serializers.data.ImageDataSerializer import ImageDataSerializer
from model.event_serializers.metadata.JsonMetadataSerializer import JsonMetadataSerializer
from model.readers.data.ImageDataReader import ImageDataReader
from model.stores.EventStore import EventStore
from model.writers.EventWriter import EventWriter
from model.writers.data.ImageDataWriter import ImageDataWriter
from model.writers.metadata.MetadataWriter import MetadataWriter

datalake = Datalake()
datalake_handler = ImageFileSystemStructureDatalakeHandler(datalake,
                                                           ImageEventIngestor(
                                                               ImageDataReader(),
                                                               EventStore(
                                                                   EventWriter(
                                                                       ImageDataWriter(),
                                                                       MetadataWriter()),
                                                                   JsonMetadataSerializer(),
                                                                   ImageDataSerializer()))
                                                           )

# datalake_handler.add_from("sources/DatasetTumoresCerebrales/test")
# datalake_handler.add_from("sources/DatasetTumoresCerebrales/training")



print(len(datalake))
