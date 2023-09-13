from typing import Optional

import pandas as pd
from sdv.tabular import GaussianCopula

from src.domain.data_generator import DataGenerator, DataGeneratorError
from src.domain.database import Database


class SdvDataGenerator(DataGenerator):
    def __init__(self, database: Database):
        self._database = database

    def _extract_sample_data(self, table: str, sample_limit: Optional[int] = 5_000):
        query = f"""
            SELECT *
            FROM
                {table}
            LIMIT {sample_limit}
        """
        with self._database.connect() as conn:
            with conn.cursor() as curr:
                header = None
                curr.execute(query)

                if curr.description is not None:
                    header = tuple(i.name for i in curr.description)
                body = curr.fetchall()

                conn.commit()
        return pd.DataFrame.from_records(body, columns=header)

    def generate(self, table: str, sample_limit: Optional[int] = 5_000, synthetic_limit: Optional[int] = 5_000):
        try:
            data = self._extract_sample_data(table=table, sample_limit=sample_limit)
            model = GaussianCopula()
            model.fit(data)
            return model.sample(synthetic_limit).to_records(index=False)
        except Exception as e:
            DataGeneratorError(f"Cannot generate data for table {table} with exception {e}")
