import psycopg2
from psycopg2 import sql

class MedicalStaff:
    def __init__(self, id, surname, address, tax):
        self.id = id
        self.surname = surname
        self.address = address
        self.tax = tax

class Requests:
    def __init__(self, conn):
        self.conn = conn

    def create_medical_staff(self, id, surname, address, tax):
        try:
            with self.conn.cursor() as cursor:
                request = sql.SQL("""
                    INSERT INTO MedicalStaff (ID, Surname, Address, Tax) 
                    VALUES (%s, %s, %s, %s) 
                    RETURNING id, surname, address, tax
                """)
                cursor.execute(request, (id, surname, address, tax))
                row = cursor.fetchone()
                return MedicalStaff(*row) if row else None

        except psycopg2.Error as e:
            print(f"Creating error: {e}")
            return None
