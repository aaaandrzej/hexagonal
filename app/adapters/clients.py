import json
import requests

from app.bl.exc import BLCantFetchDataError


def get_clients() -> list:
    try:
        with open('users.csv') as f:
            content = f.readlines()
            result = [{'name': row.strip('\n').split(';')[0], 'surname': row.strip('\n').split(';')[1]} for row in
                      content]  # TODO użyć dataclass
            return result

    except Exception:
        raise BLCantFetchDataError  # example BL exception implementation


def get_clients_from_api() -> list:
    resp = requests.get('http://localhost:8091/users')
    return json.loads(resp.content)
