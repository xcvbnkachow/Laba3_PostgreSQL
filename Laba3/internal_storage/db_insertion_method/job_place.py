import sqlite3
import csv

def insert_into_job_place(db_path):
    try:
        with open("../../src/job_place.txt", "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="\t")
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")

            for row in reader:
                if len(row) != 4:
                    print(f"Skip a line: {row}")
                    continue

                try:
                    id, office, address, local_budget_tax = int(row[0]), row[1], row[2], float(row[3])
                    cursor.execute("""
                        INSERT INTO JobPlace (ID, Office, Address, LocalBudgetTax)
                        VALUES (?, ?, ?, ?)
                    """, (id, office, address, local_budget_tax))
                except (ValueError, TypeError, sqlite3.IntegrityError) as e:
                    print(f"Ошибка при вставке строки {row}: {e}")
                    conn.rollback()
                    return False

            conn.commit()
            return True

    except FileNotFoundError:
        print("Ошибка: файл job_place.txt не найден.")
        return False
    except sqlite3.Error as e:
        print(f"Произошла некая ошибка: {e}")
        return False
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    try:
        with open("../../internal_storage/sql/db_path.txt", "r", encoding="utf-8") as f:
            db_path = f.read()
        print("Данные успешно вставлены!" if insert_into_job_place(db_path) else "К сожалению, вставка данных не удалась..")
    except FileNotFoundError:
        print(f"Ошибка: файл db_path.txt не найден.")