import abc

from src.domain.exception import DataEmulatorBaseException


class DataGeneratorError(DataEmulatorBaseException):
    ...


class DataGenerator(abc.ABC):
    def generate(self, table: str):
        ...
