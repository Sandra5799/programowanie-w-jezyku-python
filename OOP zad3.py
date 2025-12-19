class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House at {self.address}:\n"
                f"  Area: {self.area} m²\n"
                f"  Rooms: {self.rooms}\n"
                f"  Price: {self.price}\n"
                f"  Plot size: {self.plot} m²")

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat at {self.address}:\n"
                f"  Area: {self.area} m²\n"
                f"  Rooms: {self.rooms}\n"
                f"  Price: {self.price}\n"
                f"  Floor: {self.floor}")


house = House(area=100, rooms=4, price=700000, address="Zabrze, ul. Warszawska 3", plot=300)
flat = Flat(area=70, rooms=3, price=250000, address="Katowice, ul. Łokietka 2", floor=2)


print(house)
print(flat)
