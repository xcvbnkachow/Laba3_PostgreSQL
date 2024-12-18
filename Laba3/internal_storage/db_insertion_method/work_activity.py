import psycopg2
import csv

def insert_into_work_activity(db_path):
    try:
        with open("../../src/work_activity.txt", "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="\t")
            conn = psycopg2.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")

            try:
                for row in reader:
                    if len(row) != 7:
                        print(f"Skip a line: {row}")
                        continue

                    try:
                        contract = int(row[0])
                        weekday = row[1]
                        medical_id, jobplace_id, operation_id = int(row[2]), int(row[3]), int(row[4])
                        amount = int(row[5])
                        payment = float(row[6])

                        cursor.execute("""
                            INSERT INTO WorkActivity (Contract, Weekday, MedicalID, JobPlaceID, OperationID, Amount, Payment)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        """, (contract, weekday, medical_id, jobplace_id, operation_id, amount, payment))
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
        print(f"Ошибка: файл work_activity.txt не найден.")
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
        print("Данные успешно вставлены!" if insert_into_work_activity(db_path) else "К сожалению, вставка данных не удалась..")
    except FileNotFoundError:
        print(f"Ошибка: файл db_path.txt не найден.")

