from flask import Flask

from app.adapters.resources import persons, test

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_route() -> dict:
    return test()  # TODO czy takie obejście na rozdzielenie funkcji od rejestracji endpointu jest ok? falcon to robi inaczej


@app.route('/persons', methods=['GET'])
def persons_route() -> list:  # TODO czy tu w hint powinni być list czy persons?
    return persons()
