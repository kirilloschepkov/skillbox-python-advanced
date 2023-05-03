import sqlite3

with sqlite3.connect('hw_4_database.db') as conn:
    cursor = conn.cursor()

    result = cursor.execute('SELECT COUNT(*) FROM (SELECT salary FROM salaries WHERE salary<5000)').fetchone()
    print(f'{result[0]} человек с острова N находятся за чертой бедности, то есть получает меньше 5000 гульденов в год')

    result = cursor.execute('SELECT AVG(salary) FROM salaries').fetchone()
    print(f'Средняя зарплата на острове N - {result[0]}')

    salaries = cursor.execute('SELECT salary FROM salaries ORDER BY salary').fetchall()
    result = salaries[(len(salaries)) // 2]
    print(f'Медианная зарплата на острове N - {result[0]}')

    sum_salary = cursor.execute('SELECT SUM(salary) FROM salaries').fetchone()[0]
    count_salary = cursor.execute('SELECT COUNT(salary) FROM salaries').fetchone()[0]
    T = cursor.execute(f'SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {count_salary})').fetchone()[0]
    K = sum_salary - T
    F = T / K
    print(f'Социальное неравенство на острове: {F * 100:.2f}%')
