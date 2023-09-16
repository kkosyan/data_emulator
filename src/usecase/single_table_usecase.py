import logging

from src.domain.data_generator import DataGenerator
from src.domain.ddl_extractor import DdlExtractor
from src.domain.exception import DataEmulatorBaseException
from src.domain.synthetic_data_uploader import SyntheticDataUploader


class DataEmulatorForSingleTable:
    def __init__(self, synthetic_data_uploader: SyntheticDataUploader,
                 data_generator: DataGenerator, ddl_extractor: DdlExtractor):
        self._synthetic_data_uploader = synthetic_data_uploader
        self._data_generator = data_generator
        self._ddl_extractor = ddl_extractor

        self._logger = logging.getLogger(self.__class__.__name__)

    def _execute(self, table: str):
        schema_ddl = self._ddl_extractor.extract_schema(table=table)
        objects_ddl = self._ddl_extractor.extract_objects(table=table)
        ddl_query = schema_ddl + objects_ddl

        synthetic_data = self._data_generator.generate(table=table)
        self._synthetic_data_uploader.apply_ddl(ddl_query=ddl_query)
        self._synthetic_data_uploader.upload_data(table=table, data=synthetic_data)

    def execute(self, table: str):
        try:
            self._execute(table=table)
        except DataEmulatorBaseException as e:
            self._logger.exception(f'Data emulation failed with exception {e}')
