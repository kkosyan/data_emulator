import abc


class SchemaExtractor(abc.ABC):
    @abc.abstractmethod
    def extract(self):
        ...
