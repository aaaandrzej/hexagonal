from app.bl.exc import BLCantFetchDataError


class GetPersons:
    def __init__(self, client_loader, employees_loader):  # TODO czy to wymaga annotations?
        self._client_loader = client_loader
        self._employees_loader = employees_loader

    def get(self, source: int) -> list:
        if source == 1:
            try:
                result = self._client_loader()
            except BLCantFetchDataError:  # example BL exception handling
                result =[]
        elif source == 2:
            result = self._employees_loader()
        else:
            result = self._client_loader()
            result.extend(self._employees_loader())
        return result
