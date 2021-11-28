import requests

from models.Brewery import Brewery

payload = {'per_page': 20}
response = requests.get('https://api.openbrewerydb.org/breweries',
                        params=payload)

list_of_breweries = [Brewery(x) for x in response.json()]

for x in list_of_breweries:
    print(x)
