class Metadata:
    def __init__(self, directory):
        self.directory = directory


class Datalake:
    def __init__(self, directory="/datalake"):
        self.directory = directory

    def metadata(self):
        return Metadata(self.directory + "/metadata")
