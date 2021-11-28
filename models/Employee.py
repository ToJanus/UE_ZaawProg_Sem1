from datetime import datetime


class Employee:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 hire_date: datetime,
                 birth_date: datetime,
                 city: str,
                 street: str,
                 zip_code: str,
                 phone: int) -> None:
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._hire_date: datetime = hire_date
        self._birth_date: datetime = birth_date
        self._city: str = city
        self._street: str = street
        self._zip_code: str = zip_code
        self._phone: int = phone

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def hire_date(self) -> datetime:
        return self._hire_date

    @hire_date.setter
    def hire_date(self, value: datetime):
        self._hire_date = value

    @property
    def birth_date(self) -> datetime:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: datetime):
        self._birth_date = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value: str):
        self._street = value

    @property
    def zip_code(self) -> str:
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value: str):
        self._zip_code = value

    @property
    def phone(self) -> int:
        return self._phone

    @phone.setter
    def phone(self, value: int):
        self._phone = value

    def __str__(self) -> str:
        return f"{self._first_name} {self._last_name}, " \
               f"hire_date: {self._hire_date}, " \
               f"birth_date: {self._birth_date}, " \
               f"city: {self._city}, street: {self._street}, " \
               f"zip_code: {self._zip_code}, phone: {self._phone}"
