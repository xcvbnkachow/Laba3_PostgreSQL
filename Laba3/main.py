import psycopg2
import logging
from internal_storage.db_insertion_method.medical_staff import insert_into_medical_staff
from internal_storage.db_insertion_method.operation_types import insert_into_operation_types
from internal_storage.db_insertion_method.work_activity import insert_into_work_activity
from internal_storage.db_insertion_method.job_place import insert_into_job_place

logging.basicConfig(level=logging.ERROR)

class ApiRequests:
    def __init__(self, conn):
        self.conn = conn


def main():
    try:
        with open("../../internal_storage/sql/db_path.txt", "r", encoding="utf-8") as f:
            db_path = f.read()

            try:
                conn = psycopg2.connect(db_path)
                api = ApiRequests(conn)

                try:
                    insert_into_medical_staff(api.conn)
                    insert_into_job_place(api.conn)
                    insert_into_operation_types(api.conn)
                    insert_into_work_activity(api.conn)
                    conn.commit()
                    print("- Insertion success -")
                except psycopg2.Error as e:
                    conn.rollback()
                    logging.error(f"Ошибка при вставке данных: {e}")
                finally:
                    conn.close()

            except psycopg2.Error as e:
                logging.error(f"Ошибка подключения к базе данных: {e}")

    except FileNotFoundError:
        print(f"Ошибка: файл db_path.txt не найден.")


if __name__ == "__main__":
    main()
