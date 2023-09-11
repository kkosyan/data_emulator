from typing import Sequence

from src.domain.database import Database
from src.domain.synthetic_data_uploader import SyntheticDataUploader


class PostrgesSyntheticDataUploader(SyntheticDataUploader):
    def __init__(self, database: Database):
        self._database = database

    def apply_ddl(self, ddl_query: str):
        with self._database.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(ddl_query)
                conn.commit()

    def _select_columns_number(self, table: str) -> int:
        columns_number_query = f"""
                SELECT
                    count(*)
                FROM
                    information_schema.columns
                WHERE
                    table_name='{table}'
                """
        with self._database.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(columns_number_query)
                result = cur.fetchone()
                conn.commit()
        return result[0]

    def upload_data(self, table: str, data: Sequence):
        columns_number = self._select_columns_number(table=table)
        insert_query = f"""
            INSERT INTO {table}
            VALUES ({','.join(['%s'] * columns_number)})
        """
        with self._database.connect() as conn:
            with conn.cursor() as cur:
                cur.executemany(insert_query, data)
                conn.commit()
