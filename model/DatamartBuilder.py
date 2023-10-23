from abc import abstractmethod


class DatamartBuilder:
    @abstractmethod
    def build(self, datamart_path, categories):
        pass
