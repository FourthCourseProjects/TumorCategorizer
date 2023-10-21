import os


class Datalake:
    def __init__(self, directory="datalake"):
        self.directory = directory

    def metadata_tank(self):
        return self.tank("metadata")

    def tank(self, tank_route):
        return Tank(self.directory + "/" + tank_route)

    def __len__(self):
        return len(os.listdir(self.directory)) - 1


class Tank:
    def __init__(self, directory):
        self.name = directory.split("/")[-1]
        self.directory = directory
