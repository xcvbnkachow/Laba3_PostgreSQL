import psycopg2
from contextlib import contextmanager

class DB:
    def execute(self, request, *params):
        raise NotImplementedError
    def executemany(self, request, param_list):
        raise NotImplementedError
    def fetchall(self, request, *params):
        raise NotImplementedError
    def fetchone(self, request, *params):
        raise NotImplementedError

class Requests:
    def __init__(self, db: DB):
        self.db = db

    @contextmanager
    def with_TX(self, tx):
        db_ = self.db
        self.db = tx
        try: yield self
        finally: self.db = db_

class PostgreSQL_DB(DB):
    def __init__(self, db_path):
        self.connection = psycopg2.connect(db_path)

    def execute(self, query, *params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.lastrowid

    def executemany(self, query, param_list):
        cursor = self.connection.cursor()
        cursor.executemany(query, param_list)
        self.connection.commit()

    def fetchall(self, query, *params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def fetchone(self, query, *params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
