import psycopg2
import csv

def insert_into_operation_types(db_path):
    try:
        with open("../../src/operation_types.txt", "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="\t")
            conn = psycopg2.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")

            try:
                for row in reader:
                    if len(row) != 5:
                        print(f"Skip a line: {row}")
                        continue

                    try:
                        id, name, strong_point, stocks, cost = int(row[0]), row[1], row[2], int(row[3]), float(row[4])
                        cursor.execute("""
                            INSERT INTO OperationTypes (ID, Name, StrongPoint, Stocks, Cost)
                            VALUES (?, ?, ?, ?, ?)
                        """, (id, name, strong_point, stocks, cost))
                    except (ValueError, TypeError, psycopg2.IntegrityError) as e:
                        print(f"Ошибка при вставке строки {row}: {e}")
                        conn.rollback()
                        return False

                conn.commit()
                return True

            except psycopg2.Error as e:
                print(f"Ошибка PostgreSQL: {e}")
                return False

    except FileNotFoundError:
        print(f"Ошибка: файл operation_types.txt.txt не найден.")
        return False
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return False
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


if __name__ == "__main__":
    try:
        with open("../../internal_storage/sql/db_path.txt", "r", encoding="utf-8") as f:
            db_path = f.read()
        print("Данные успешно вставлены!" if insert_into_operation_types(db_path) else "К сожалению, вставка данных не удалась..")
    except FileNotFoundError:
        print(f"Ошибка: файл db_path.txt не найден.")


