import pandas as pd
import pytest
from sdv.evaluation import evaluate

from src.app.config import get_settings
from src.domain.database import PostgresDatabase

settings = get_settings(env_for_dynaconf='testing')
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


class TestService:
    @staticmethod
    def _get_db_data(database: PostgresDatabase):
        with database.connect() as conn:
            with conn.cursor() as curr:
                header = None
                curr.execute("""
                    SELECT *
                    FROM
                        users
                """)

                if curr.description is not None:
                    header = tuple(i.name for i in curr.description)
                body = curr.fetchall()

                conn.commit()
        return pd.DataFrame.from_records(body, columns=header)

    @pytest.mark.e2e
    def test_emulation_quality(self):
        sample_data = self._get_db_data(database=sample_database)
        synthetic_data = self._get_db_data(database=synthetic_database)

        quality_report = evaluate(sample_data, synthetic_data, metrics=['CSTest', 'KSTest'], aggregate=False)

        assert quality_report.get_value('CSTest', 'normalized_score') >= 0.5
        assert quality_report.get_value('KSTest', 'normalized_score') >= 0.5
