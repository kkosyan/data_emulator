import dynaconf

from src.domain.database import PostgresDatabase
from src.infrastructure.ddl_extractors import PostgresDdlExtractor
from src.infrastructure.sdv_data_generator import SdvDataGenerator
from src.infrastructure.synthetic_data_uploaders import PostgresSyntheticDataUploader
from src.usecase.single_table_usecase import DataEmulatorForSingleTable


class Context:
    data_emulator_for_single_table: DataEmulatorForSingleTable


class LocalContext(Context):
    def __init__(self, settings: dynaconf.Dynaconf):
        database_config = {
            'host': settings.db.host,
            'port': settings.db.port,
            'database': settings.db.database,
            'user': settings.db.user,
            'password': settings.db.password,

        }
        database = PostgresDatabase(**database_config)

        synthetic_data_uploader = PostgresSyntheticDataUploader(
            database=database,
        )
        data_generator = SdvDataGenerator(
            database=database,
        )
        ddl_extractor = PostgresDdlExtractor(**database_config)

        self.data_emulator_for_single_table = DataEmulatorForSingleTable(
            database=database,
            synthetic_data_uploader=synthetic_data_uploader,
            data_generator=data_generator,
            ddl_extractor=ddl_extractor,
        )
