class Metadata:
    def __init__(self, directory):
        self.directory = directory


class Datalake:
    def __init__(self, directory="/datalake"):
        self.directory = directory

    def metadata_tank(self):
        return self.tank("metadata")

    def tank(self, tank_route):
        return Tank(self.directory + "/" + tank_route)


class Tank:
    def __init__(self, directory):
        self.directory = directory
