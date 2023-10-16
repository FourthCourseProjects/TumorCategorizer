class Dataset:
    def __init__(self, entries, batch_size=5):
        self.entries = entries
        self.batch_size = batch_size
