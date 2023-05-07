import sqlite3

# Создаем подключение к базе данных и создаем таблицу
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# создаем таблицу employee
cursor.execute('''CREATE TABLE IF NOT EXISTS employee
               (id INTEGER PRIMARY KEY,
                name VARCHAR
                )
                ''')

# создаем таблицу sales
cursor.execute('''CREATE TABLE IF NOT EXISTS sales
               (id INTEGER PRIMARY KEY,
                employee_id INTEGER,
                price INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employee(id)
                )
                ''')

employees = [("Андрей",), ("Иван",), ("Лиза",), ("Катя",)]
cursor.executemany("INSERT INTO employee (name) VALUES (?)", employees)

sales = [(1, 100), (2, 150), (3, 200), (4, 50), (1, 100), (2, 300), (3, 250), (4, 50), (1, 100), (1, 50)]
cursor.executemany("INSERT INTO sales (employee_id, price) VALUES (?, ?)", sales)

# создаем таблицу transfers
cursor.execute('''CREATE TABLE transfers
               (from_acc INTEGER, to_acc INTEGER, amount INTEGER, tdate TEXT)''')

cursor.execute("INSERT INTO transfers VALUES (?, ?, ?, ?)", (1, 2, 500, '23.02.2023'))
cursor.execute("INSERT INTO transfers VALUES (?, ?, ?, ?)", (2, 3, 300, '01.03.2023'))
cursor.execute("INSERT INTO transfers VALUES (?, ?, ?, ?)", (3, 1, 200, '05.03.2023'))
cursor.execute("INSERT INTO transfers VALUES (?, ?, ?, ?)", (1, 3, 400, '05.04.2023'))


conn.commit()
conn.close()
