class Library:
    def __init__(
            self,
            city: str,
            street: str,
            zip_code: str,
            open_hours: str,
            phone: int) -> None:
        self._city: str = city
        self._street: str = street
        self._zip_code: str = zip_code
        self._open_hours: str = open_hours
        self._phone: int = phone

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value: str) -> None:
        self._street = value

    @property
    def zip_code(self) -> str:
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value: str) -> None:
        self._zip_code = value

    @property
    def open_hours(self) -> str:
        return self._open_hours

    @open_hours.setter
    def open_hours(self, value: str) -> None:
        self._open_hours = value

    @property
    def phone(self) -> int:
        return self._phone

    @phone.setter
    def phone(self, value: int) -> None:
        self._phone = value

    def __str__(self) -> str:
        return f"city: {self._city}, " \
               f"street: {self._street}, " \
               f"zip_code: {self._zip_code}, " \
               f"open_hours: {self._open_hours}, " \
               f"phone: {self._phone}"
