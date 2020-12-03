from flask import jsonify, request

from app.core.factory import Factory


def test() -> dict:
    return jsonify({'hello': 'world'})


def persons() -> list:
    source = int(request.args.get('source', 1))

    bl = Factory.get_persons_query()
    result = bl.get(source)

    format = request.args.get('format', 'json')
    if format == 'json':
        return jsonify(result)
    elif format == 'csv':
        return jsonify([{'to be': 'implemented'}])  # potential app extension
