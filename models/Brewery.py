from datetime import datetime


class Brewery:
    def __init__(self, dict_with_values: dict):
        self.id: str = dict_with_values['id']
        self.name: str = dict_with_values['name']
        self.brewery_type: str = dict_with_values['brewery_type']
        self.street: str = dict_with_values['street']
        self.address_2 = dict_with_values['address_2']
        self.address_3 = dict_with_values['address_3']
        self.city: str = dict_with_values['city']
        self.state: str = dict_with_values['state']
        self.county_province = dict_with_values['county_province']
        self.postal_code: str = dict_with_values['postal_code']
        self.country: str = dict_with_values['country']
        self.longitude: float = float(dict_with_values['longitude'])
        self.latitude: float = float(dict_with_values['latitude'])
        self.phone: int = int(dict_with_values['phone'])
        self.website_url = dict_with_values['website_url']
        self.updated_at: datetime = datetime.strptime(dict_with_values['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        self.created_at: datetime = datetime.strptime(dict_with_values['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}\n" \
               f"Street: {self.street}, City: {self.city}, " \
               f"State: {self.state}, Code: {self.postal_code}"
