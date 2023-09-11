import re
import subprocess

from src.domain.ddl_extractor import DdlExtractor


class PostgresSchemaExtractor(DdlExtractor):
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._dbname = database
        self._user = user
        self._password = password

    def _get_dump(self, table: str) -> bytes:
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

        return output

    def extract_schema(self, table: str) -> str:
        dump = self._get_dump(table=table)
        return re.search("Schema: \w+", dump.decode()).group().split()[1]

    def extract_objects(self, table: str) -> list[str]:
        dump = self._get_dump(table=table)
        return re.findall("CREATE .*?;|ALTER (?!.*OWNER TO).*?;", dump.decode(), flags=re.DOTALL)
