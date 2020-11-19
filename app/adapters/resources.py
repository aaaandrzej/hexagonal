from flask import jsonify, request
import sqlite3


def test() -> dict:
    return jsonify({'hello': 'world'})


def persons() -> dict:
    source = int(request.args.get('source', 1))  # TODO czy to powinienem wynieść do persons_route i przekazywać jako zmienną?
    if source == 1:
        with open('users.csv') as f:
            content = f.readlines()
            result = [{'name': row.strip('\n').split(';')[0], 'surname': row.strip('\n').split(';')[1]} for row in content]
            return jsonify(result)
    elif source == 2:
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
        return jsonify(result)