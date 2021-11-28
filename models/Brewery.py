from datetime import datetime


class Brewery:
    def __init__(self, dict_with_values: dict):
        self._id: str = dict_with_values['id'] \
            if dict_with_values['id'] is not None else None
        self._name: str = dict_with_values['name'] \
            if dict_with_values['name'] is not None else None
        self._brewery_type: str = dict_with_values['brewery_type'] \
            if dict_with_values['brewery_type'] is not None else None
        self._street: str = dict_with_values['street'] \
            if dict_with_values['street'] is not None else None
        self._address_2: str = dict_with_values['address_2'] \
            if dict_with_values['address_2'] is not None else None
        self._address_3: str = dict_with_values['address_3'] \
            if dict_with_values['address_3'] is not None else None
        self._city: str = dict_with_values['city'] \
            if dict_with_values['city'] is not None else None
        self._state: str = dict_with_values['state'] \
            if dict_with_values['state'] is not None else None
        self._county_province: str = dict_with_values['county_province'] \
            if dict_with_values['county_province'] is not None else None
        self._postal_code: str = dict_with_values['postal_code'] \
            if dict_with_values['postal_code'] is not None else None
        self._country: str = dict_with_values['country'] \
            if dict_with_values['country'] is not None else None
        self._longitude: float = float(dict_with_values['longitude']) \
            if dict_with_values['longitude'] is not None else None
        self._latitude: float = float(dict_with_values['latitude']) \
            if dict_with_values['latitude'] is not None else None
        self._phone: float = float(dict_with_values['phone']) \
            if dict_with_values['phone'] is not None else None
        self._website_url: str = dict_with_values['website_url'] \
            if dict_with_values['website_url'] is not None else None
        self._updated_at: datetime = datetime.strptime(
            dict_with_values['updated_at'],
            '%Y-%m-%dT%H:%M:%S.%fZ') \
            if dict_with_values['updated_at'] is not None else None
        self._created_at: datetime = datetime.strptime(
            dict_with_values['created_at'],
            '%Y-%m-%dT%H:%M:%S.%fZ') \
            if dict_with_values['created_at'] is not None else None

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def brewery_type(self) -> str:
        return self._brewery_type

    @brewery_type.setter
    def brewery_type(self, value: str) -> None:
        self._brewery_type = value

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value: str) -> None:
        self._street = value

    @property
    def address_2(self) -> str:
        return self._address_2

    @address_2.setter
    def address_2(self, value: str) -> None:
        self._address_2 = value

    @property
    def address_3(self) -> str:
        return self._address_3

    @address_3.setter
    def address_3(self, value: str) -> None:
        self._address_3 = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value

    @property
    def county_province(self) -> str:
        return self._county_province

    @county_province.setter
    def county_province(self, value: str) -> None:
        self._county_province = value

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value: str) -> None:
        self._postal_code = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str) -> None:
        self._country = value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, value: float) -> None:
        self._longitude = value

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, value: float) -> None:
        self._latitude = value

    @property
    def phone(self) -> int:
        return self._phone

    @phone.setter
    def phone(self, value: int) -> None:
        self._phone = value

    @property
    def website_url(self) -> str:
        return self._website_url

    @website_url.setter
    def website_url(self, value: str) -> None:
        self._website_url = value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value: datetime) -> None:
        self._updated_at = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        self._created_at = value

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}\n" \
               f"Street: {self.street}, City: {self.city}, " \
               f"State: {self.state}, Code: {self.postal_code}"
