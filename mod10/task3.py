import sqlite3

with sqlite3.connect('hw_3_database.db') as conn:
    cursor = conn.cursor()

    for number_table in range(1, 4):
        result = cursor.execute(f'SELECT COUNT(*) FROM table_{number_table}').fetchone()
        print(f'Записей в table_{number_table} - {result[0]}')

    result = cursor.execute('SELECT COUNT(DISTINCT value) FROM table_1').fetchone()
    print(f'Уникальных записей в таблице table_1 - {result[0]}')

    result = cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2)").fetchone()
    print(f'Записей из таблицы table_1 встречается в table_2 - {result[0]}')

    result = cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2) AND value IN (SELECT value FROM table_3)").fetchone()
    print(f'Записей из таблицы table_1 встречается и в table_2, и в table_3 - {result[0]}')
