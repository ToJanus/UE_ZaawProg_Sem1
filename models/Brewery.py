class Brewery:
    def __init__(self, dict_with_values):
        self.id = dict_with_values['id']
        self.name = dict_with_values['name']
        self.brewery_type = dict_with_values['brewery_type']
        self.street = dict_with_values['street']
        self.address_2 = dict_with_values['address_2']
        self.address_3 = dict_with_values['address_3']
        self.city = dict_with_values['city']
        self.state = dict_with_values['state']
        self.county_province = dict_with_values['county_province']
        self.postal_code = dict_with_values['postal_code']
        self.country = dict_with_values['country']
        self.longitude = dict_with_values['longitude']
        self.latitude = dict_with_values['latitude']
        self.phone = dict_with_values['phone']
        self.website_url = dict_with_values['website_url']
        self.updated_at = dict_with_values['updated_at']
        self.created_at = dict_with_values['created_at']

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}\n" \
               f"Street: {self.street}, City: {self.city}, " \
               f"State: {self.state}, Code: {self.postal_code}"
