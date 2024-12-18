import psycopg2
from psycopg2 import sql

class WorkActivity:
    def __init__(self, contract, weekday, medical_id, jobplace_id, operation_id, amount, payment):
        self.contract = contract
        self.weekday = weekday
        self.medical_id = medical_id
        self.jobplace_id = jobplace_id
        self.operation_id = operation_id
        self.amount = amount
        self.payment = payment

class Requests:
    def __init__(self, conn):
        self.conn = conn

    def create_work_activity(self, contract, weekday, medical_id, jobplace_id, operation_id, amount, payment):
        try:
            with self.conn.cursor() as cursor:
                request = sql.SQL("""
                    INSERT INTO WorkActivity (Contract, Weekday, MedicalID, JobPlaceID, OperationID, Amount, Payment)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING contract, weekday, medical_id, jobplace_id, operation_id, amount, payment
                """)
                cursor.execute(request, (contract, weekday, medical_id, jobplace_id, operation_id, amount, payment))
                row = cursor.fetchone()
                return WorkActivity(*row) if row else None

        except psycopg2.Error as e:
            print(f"Creating error: {e}")
            return None
