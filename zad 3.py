class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość: {self.address}, {self.area} m², {self.rooms} pokoi, cena: {self.price}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom: {self.address}, {self.area} m², {self.rooms} pokoi, działka: {self.plot} m², cena: {self.price}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie: {self.address}, {self.area} m², {self.rooms} pokoi, piętro: {self.floor}, cena: {self.price}"


# Tworzenie obiektów
house1 = House(120, 5, 500000, "ul. Polna 3, Warszawa", 500)
flat1 = Flat(60, 3, 300000, "ul. Długa 7, Kraków", 2)

print(house1)
print(flat1)
