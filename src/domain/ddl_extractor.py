import abc

from src.domain.exception import DataEmulatorBaseException


class DdlExtractorError(DataEmulatorBaseException):
    ...


class DdlExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_schema(self, table: str) -> str:
        ...

    @abc.abstractmethod
    def extract_objects(self, table: str) -> str:
        ...
