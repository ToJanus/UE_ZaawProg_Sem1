import requests
import argparse

from models.Brewery import Brewery

parser = argparse.ArgumentParser()
parser.add_argument('--city', type=str, default=None)
args = parser.parse_args()

city = str(args.city).replace(' ', '_')
if args.city is None:
    payload = {'per_page': 20}
else:
    payload = {'per_page': 20, 'by_city': city}

response = requests.get('https://api.openbrewerydb.org/breweries',
                        params=payload)

list_of_breweries = [Brewery(x) for x in response.json()]
for x in list_of_breweries:
    print(x)
