from decimal import *
getcontext().prec = 2


class Property:
    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area: str = area
        self.rooms: int = rooms
        self.price: Decimal = Decimal(str(price))
        self.address: str = address

    def __str__(self) -> str:
        return f"area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}"

class House(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot: int = plot

    def __str__(self) -> str:
        return f"Property of house -> {super().__str__()}, plot: {self.plot}"

class Flat(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor: int = floor

    def __str__(self) -> str:
        return f"Property of flat -> {super().__str__()}, floor: {self.floor}\n"


if __name__ == "__main__":
    flat = Flat(area='Area1',
                rooms=4,
                price=1999.99,
                address='Address1',
                floor=1)
    house = House(area='Area2',
                  rooms=3,
                  price=6999.99,
                  address='Address2',
                  plot=98)
    print(flat)
    print(house)
