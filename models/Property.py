from decimal import Decimal


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
