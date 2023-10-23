from model.Datalake import Datalake
from model.DatalakeQuerier import DatalakeQuerier
from model.Reader import Reader
from model.datamart_builders.ImageFileSystemDatamartBuilder import ImageFileSystemDatamartBuilder
from model.event_deserializers.metadata.JsonMetadataDeserializer import JsonMetadataDeserializer
from model.readers.DatalakeMetadataReader import DatalakeMetadataReader
from model.readers.data.ImageReader import ImageReader
from model.writers.data.ImageDataWriter import ImageDataWriter

path = "datalake/metadata/9a0b936e-71d3-11ee-a088-8c85907d7145.metadata"
reader = DatalakeMetadataReader(Reader(), JsonMetadataDeserializer())
datalake = Datalake()
querier = DatalakeQuerier(reader, datalake)
ImageFileSystemDatamartBuilder(ImageReader(), DatalakeMetadataReader(Reader(), JsonMetadataDeserializer()),
                               DatalakeQuerier(reader, datalake), ImageDataWriter(), datalake).build("datamart",
                                                                                                     ["Glioma", "Meningioma", "Pituitary tumor"])

