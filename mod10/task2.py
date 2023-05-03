import sqlite3

with sqlite3.connect('hw_2_database.db') as conn:
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count DESC").fetchone()
    print(f"Телефоны {result[0]} цвета покупают чаще всего")

    result = cursor.execute("SELECT * FROM table_checkout WHERE phone_color IN ('Red','Blue') ORDER BY sold_count DESC").fetchall()
    print("Телефонов красного и синего цвета покупают одинаково" if result[0][1] == result[1][1] else f"Чаще покупают телефоны цвета - {result[0][0]}")

    result = cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count").fetchone()
    print(f"Cамый непопулярный цвет телефона - {result[0]}")
