from model.Dataframe import Dataframe


class OneHotMapper:
    def apply(self, dataframe: Dataframe, column_name):
        for category in self._categories(column_name, dataframe):
            dataframe.add(category, self._values(dataframe.get()[column_name], category))

    def _categories(self, column_name, dataframe):
        return set(dataframe.get()[column_name])

    def _values(self, category_column, category):
        return [1 if value == category else 0 for value in category_column]
