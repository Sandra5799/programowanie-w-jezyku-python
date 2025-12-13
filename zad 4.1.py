import requests
import argparse

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, street: str, city: str, state: str, postal_code: str, country: str, phone: str, website_url: str):
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
        return (
            f"Brewery:\n"
            f"  Name: {self.name}\n"
            f"  Type: {self.brewery_type}\n"
            f"  Address: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
            f"  Phone: {self.phone}\n"
            f"  Website: {self.website_url}\n"
        )

def fetch_breweries(city=None):
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    if city:
        url += f"&by_city={city}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    breweries = []
    for item in data:
        breweries.append(Brewery(
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
        ))
    return breweries

def main():
    parser = argparse.ArgumentParser(description="Fetch breweries from Open Brewery DB")
    parser.add_argument("--city", type=str, help="Filter breweries by city")
    args = parser.parse_args()

    breweries = fetch_breweries(args.city)
    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()
