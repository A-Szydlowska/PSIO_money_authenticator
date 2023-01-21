import sqlite3

conn = sqlite3.connect('money.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS money (
        id INTEGER PRIMARY KEY,
        file_name TEXT,
        result TEXT,
        best_frame BLOB
    )
''')

conn.commit()
file_name = 0
result = 0


def save_to_db(file_name, result, best_frame):
    cursor.execute('''
        INSERT INTO money (file_name, result, best_frame)
        VALUES (?, ?, ?)
    ''', (file_name, result, best_frame))
    conn.commit()


def get_best_frame(file_name):
    cursor.execute('''
        SELECT best_frame FROM money
        WHERE file_name = ?
    ''', (file_name,))
    return cursor.fetchone()


best_frame = get_best_frame(file_name)
save_to_db(file_name, result, best_frame)

cursor.close()
conn.close()
'''
#wyswietlenie rekordow z bazy
import money_database

conn = sqlite3.connect('money.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM money")
records = cursor.fetchall()

for record in records:
    print(record)

conn.close()
'''