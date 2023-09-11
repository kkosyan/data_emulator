import abc


class DdlExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_schema(self, table: str) -> str:
        ...

    @abc.abstractmethod
    def extract_objects(self, table: str) -> str:
        ...
