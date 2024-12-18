import psycopg2
from psycopg2 import sql

class JobPlace:
    def __init__(self, id, office, address, local_budget_tax):
        self.id = id
        self.office = office
        self.address = address
        self.local_budget_tax = local_budget_tax

class Requests:
    def __init__(self, conn):
        self.conn = conn

    def create_job_place(self, id, office, address, local_budget_tax):
        try:
            with self.conn.cursor() as cursor:
                request = sql.SQL("""
                    INSERT INTO JobPlace (ID, Office, Address, LocalBudgetTax)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, office, address, local_budget_tax
                """)
                cursor.execute(request, (id, office, address, local_budget_tax))
                row = cursor.fetchone()
                return JobPlace(*row) if row else None

        except psycopg2.Error as e:
            print(f"Creating error: {e}")
            return None
