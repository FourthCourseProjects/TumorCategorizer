import random


class Dataset:
    def __init__(self, entries, batch_size=5):
        self.entries = entries
        self.batch_size = batch_size

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > len(self.entries) - 1: raise StopIteration
        entry = self.entries[self.index]
        self.index += 1
        return entry.input, entry.output

    def shuffle(self):
        random.shuffle(self.entries)
