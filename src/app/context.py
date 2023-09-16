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
        sample_database_config = {
            'host': settings.sample_db.host,
            'port': settings.sample_db.port,
            'database': settings.sample_db.database,
            'user': settings.sample_db.user,
            'password': settings.sample_db.password,
        }
        synthetic_database_config = {
            'host': settings.synthetic_db.host,
            'port': settings.synthetic_db.port,
            'database': settings.synthetic_db.database,
            'user': settings.synthetic_db.user,
            'password': settings.synthetic_db.password,
        }
        sample_database = PostgresDatabase(**sample_database_config)
        synthetic_database = PostgresDatabase(**synthetic_database_config)

        synthetic_data_uploader = PostgresSyntheticDataUploader(
            database=synthetic_database,
        )
        data_generator = SdvDataGenerator(
            database=sample_database,
        )
        ddl_extractor = PostgresDdlExtractor(**sample_database_config)

        self.data_emulator_for_single_table = DataEmulatorForSingleTable(
            database=sample_database,
            synthetic_data_uploader=synthetic_data_uploader,
            data_generator=data_generator,
            ddl_extractor=ddl_extractor,
        )
