from flask import Flask

from app.adapters.resources import persons, test

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_route() -> dict:
    return test()


@app.route('/persons', methods=['GET'])
def persons_route() -> list:
    return persons()
