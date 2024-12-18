Лабораторная работа №3 | Вариант №4  


Исходные данные для работы с таблицами находятся в папке src  
Запросы: SQL_requests/requests.txt  
Реализация метода создания: internal_storage/db_creating_method  
Реализация метода вставки: internal_storage/db_insertion_method  
Путь к запросам на создание таблиц: internal_storage/sql/patterns  
Путь к запросам на вставку находятся: internal_storage/sql/requests  
Путь к db_url: internal_storage/sql/db_path.txt   

Таблица MedicalStaff:  
id SERIAL INT PRIMARY KEY: уникальный автоматически увеличивающийся ключ  
surname VARCHAR(30) NOT NULL: фамилия в основном состоит до 30 символов  
address VARCHAR(70) NOT NULL: 70 символов должно хватить, чтобы записать адрес  
tax NUMERIC(4, 2) NOT NULL CHECK (tax >= 0): налог - вещественное неотрицательное число с 4 цифрами с округлением до 2 знаков после запятой  

Таблица OperationTypes:  
id SERIAL INT PRIMARY KEY: уникальный автоматически увеличивающийся ключ  
name VARCHAR(30) NOT NULL: имя до 30 знаков, как и фамилия  
strong_point VARCHAR(70) NOT NULL: 70 символов должно хватить, чтобы записать название опорного пункта  
stocks INTEGER NOT NULL CHECK (Stock >= 0): запасы - целое неотрицательное число  
сost NUMERIC(10, 2) NOT NULL CHECK (Cost >= 0): стоимость - вещественное неотрицательное число с 10 цифрами с округлением до 2 знаков после запятой  

Таблица WorkActivity:  
contract SERIAL PRIMARY KEY: уникальный номер контракта  
weekday VARCHAR(15) NOT NULL: так как слово "Понедельник" является самым длинным словом из всех дней недели и содержит 11 букв, возьмём с запасом до 15 символов  
medical_id INTEGER NOT NULL REFERENCES MedicalStaff(id): cсылка на медперсонал  
jobplace_id INTEGER NOT NULL REFERENCES JobPlace(id): cсылка на место работы  
operation_id INTEGER REFERENCES OperationTypes(id): cсылка на тип операции  
amount INTEGER NOT NULL CHECK (amount >= 0): количество выполненных операций - целое неотрицательное число  
payment NUMERIC(10, 2) NOT NULL CHECK (payment >= 0): оплата за операцию - вещественное неотрицательное число с 10 цифрами с округлением до 2 знаков после запятой  

Таблица JobPlace:  
id SERIAL INT PRIMARY KEY: уникальный автоматически увеличивающийся ключ  
office VARCHAR(50) NOT NULL: название учреждения должно укладываться в 50 символов  
address VARCHAR(70) NOT NULL: 70 символов должно хватить, чтобы записать адрес  
local_budget_tax NUMERIC(4, 2) NOT NULL CHECK (local_budget_tax >= 0): местный налог - вещественное неотрицательное число с 4 цифрами с округлением до 2 знаков после запятой  



