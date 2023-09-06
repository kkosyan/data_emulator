import abc

import psycopg2


class Database(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        ...


class PostgresDatabase(Database):
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._dbname = database
        self._user = user
        self._password = password

    def connect(self):
        return psycopg2.connect(
            dbname=self._dbname,
            user=self._user,
            password=self._password,
            host=self._host,
            port=self._port,
        )
