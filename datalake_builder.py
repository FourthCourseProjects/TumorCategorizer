from model.Datalake import Datalake
from model.datalake_builders.ImageFileSystemStructureDatalakeBuilder import ImageFileSystemStructureDatalakeBuilder
from model.datalake_ingestors.ImageEventIngestor import ImageEventIngestor
from model.event_serializers.data.ImageDataSerializer import ImageDataSerializer
from model.event_serializers.metadata.JsonMetadataSerializer import JsonMetadataSerializer
from model.readers.ImageEventReader import ImageEventReader
from model.stores.EventStore import EventStore
from model.writers.EventWriter import EventWriter
from model.writers.data.ImageDataWriter import ImageDataWriter
from model.writers.metadata.MetadataWriter import MetadataWriter

datalake = Datalake()
datalake_handler = ImageFileSystemStructureDatalakeBuilder(datalake,
                                                           ImageEventIngestor(
                                                               ImageEventReader(),
                                                               EventStore(
                                                                   EventWriter(
                                                                       ImageDataWriter(),
                                                                       MetadataWriter()),
                                                                   JsonMetadataSerializer(),
                                                                   ImageDataSerializer()))
                                                           )

datalake_handler.add_from("sources/DatasetTumoresCerebrales/test")
datalake_handler.add_from("sources/DatasetTumoresCerebrales/training")

