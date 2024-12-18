import psycopg2
from psycopg2 import sql

class OperationTypes:
    def __init__(self, id, name, strong_point, stocks, cost):
        self.id = id
        self.name = name
        self.strong_point = strong_point
        self.stocks = stocks
        self.cost = cost

class Requests:
    def __init__(self, conn):
        self.conn = conn

    def create_operation_types(self, id, name, strong_point, stocks, cost):
        try:
            with self.conn.cursor() as cursor:
                request = sql.SQL("""
                    INSERT INTO OperationTypes (ID, Name, StrongPoint, Stocks, Cost)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id, name, strong_point, stocks, cost
                """)
                cursor.execute(request, (id, name, strong_point, stocks, cost))
                row = cursor.fetchone()
                return OperationTypes(*row) if row else None

        except psycopg2.Error as e:
            print(f"Creating error: {e}")
            return None
