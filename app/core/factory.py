from app.adapters.clients import get_clients, get_clients_from_api
from app.adapters.employees import get_employees
from app.bl.persons import GetPersons


class Factory:
    @staticmethod
    def get_persons_query():
        # return GetPersons(get_clients, get_employees)
        return GetPersons(get_clients_from_api, get_employees)