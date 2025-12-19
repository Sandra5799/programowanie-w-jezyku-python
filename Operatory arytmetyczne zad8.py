from typing import List
import requests
import argparse

URL_API = 'https://api.openbrewerydb.org/v1/breweries'

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str,
                 street: str, city: str, state: str,
                 postal_code: str, country: str,
                 phone: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (f"Brewery: {self.name} ({self.brewery_type})\n"
                f"Adres: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
                f"Telefon: {self.phone}\n"
                f"Strona www: {self.website_url}\n")

def get_breweries_from_api(city: str|None = None) -> list:
    url = f"{URL_API}?per_page=20"
    if city:
        url += f"&by_city={city}"
    return requests.get(url).json()

def brewery_factory(breweries: list) -> List[Brewery]:
    lista_browarow = []
    for item in breweries:
        browar = Brewery(
            id=item.get("id", ""),
            name=item.get("name", ""),
            brewery_type=item.get("brewery_type", ""),
            street=item.get("street", ""),
            city=item.get("city", ""),
            state=item.get("state", ""),
            postal_code=item.get("postal_code", ""),
            country=item.get("country", ""),
            phone=item.get("phone", ""),
            website_url=item.get("website_url", "")
        )
        lista_browarow.append(browar)
    return lista_browarow

def get_args():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-c', '--city', help='Filter brewery by city', required=False)
    return vars(parser.parse_args())


def main():
    args = get_args()
    breweries = get_breweries_from_api(city=args['city'])

    print(f'{breweries}')
    print(f'{len(breweries)}')

main()
