import sqlite3


def get_employees() -> list:
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('select name, surname from users')
    db_results = cursor.fetchall()
    result = []
    for row in db_results:
        result.append({
            'name': row[0],
            'surname': row[1]
        })
    return result
