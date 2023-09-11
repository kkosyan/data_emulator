import abc


class DataGenerator(abc.ABC):
    def generate(self, table: str):
        ...
