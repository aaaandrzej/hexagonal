from flask import Flask, jsonify

api = Flask(__name__)


@api.route('/users', methods=['GET'])
def users():
    return jsonify([{'name': 'Jacek', 'surname': 'Placek'}])


if __name__ == '__main__':
    api.run('127.0.0.1', port=8091, debug=True)
