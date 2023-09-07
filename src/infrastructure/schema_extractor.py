from src.domain.schema_extractor import SchemaExtractor
from src.domain.database import Database


class PostgresSchemaExtractor(SchemaExtractor):

    def __init__(self, database: Database):
        self._database = database

    def extract(self, query: str) -> str:
        ...
