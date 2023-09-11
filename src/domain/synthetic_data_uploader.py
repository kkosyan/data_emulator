import abc
from typing import Sequence


class SyntheticDataUploader(abc.ABC):
    def apply_ddl(self, ddl_query: str):
        ...

    def upload_data(self, table: str, data: Sequence):
        ...
