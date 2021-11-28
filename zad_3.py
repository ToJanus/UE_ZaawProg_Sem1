from decimal import *
getcontext().prec = 2


class Property:
    def __init__(self,
                 area: str,
                 rooms: int,
                 price: float,
                 address: str) -> None:
        self._area: str = area
        self._rooms: int = rooms
        self._price: Decimal = Decimal(str(price))
        self._address: str = address

    @property
    def area(self) -> str:
        return self._area

    @area.setter
    def area(self, value: str) -> None:
        self._area = value

    @property
    def rooms(self) -> int:
        return self._rooms

    @rooms.setter
    def rooms(self, value: int) -> None:
        self._rooms = value

    @property
    def price(self) -> Decimal:
        return self._price

    @price.setter
    def price(self, value: Decimal) -> None:
        self._price = Decimal(str(value))

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value

    def __str__(self) -> str:
        return f"area: {self.area}, rooms: {self.rooms}, " \
               f"price: {self.price}, address: {self.address}"


class House(Property):
    def __init__(self,
                 area: str,
                 rooms: int,
                 price: float,
                 address: str,
                 plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self._plot: int = plot

    @property
    def plot(self) -> int:
        return self._plot

    @plot.setter
    def plot(self, value: int) -> None:
        self._plot = value

    def __str__(self) -> str:
        return f"Property of house -> {super().__str__()}, plot: {self.plot}"


class Flat(Property):
    def __init__(self,
                 area: str,
                 rooms: int,
                 price: float,
                 address: str,
                 floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self._floor: int = floor

    @property
    def floor(self) -> int:
        return self._floor

    @floor.setter
    def floor(self, value: int) -> None:
        self._floor = value

    def __str__(self) -> str:
        return f"Property of flat -> {super().__str__()}, " \
               f"floor: {self.floor}\n"


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
