class Writer:
    def write(self, path, data):
        with open(path, "w") as file:
            file.write(data)
