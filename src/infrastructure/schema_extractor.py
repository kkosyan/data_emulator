import re
import subprocess

from src.domain.schema_extractor import SchemaExtractor


class PostgresSchemaExtractor(SchemaExtractor):
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._dbname = database
        self._user = user
        self._password = password

    def extract(self, table: str) -> str:
        pg_dump_proc = subprocess.Popen(
            ['pg_dump',
             f"--dbname=postgresql://{self._user}:{self._password}@{self._host}:{self._port}/{self._dbname}",
             "--schema-only",
             "-t",
             f"{table}",
             ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output, err = pg_dump_proc.communicate()

        return re.search("Schema: \w+", output.decode()).group().split()[1]
