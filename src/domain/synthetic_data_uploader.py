import abc
from typing import Sequence

from src.domain.exception import DataEmulatorBaseException


class SyntheticDataUploaderError(DataEmulatorBaseException):
    ...


class SyntheticDataUploader(abc.ABC):
    def apply_ddl(self, ddl_query: str):
        ...

    def upload_data(self, table: str, data: Sequence):
        ...
