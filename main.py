from model.ImageJsonSerializer import ImageJsonSerializer
from model.data_types.Image import Image
from model.datalake_builders.ImageFileSystemStructureDatalakeHandler import ImageFileSystemStructureDatalakeHandler

ImageFileSystemStructureDatalakeHandler("datalake", None).build_from("sources/DatasetTumoresCerebrales/test")
ImageJsonSerializer().serialize(Image("/directory", "Glia"))
