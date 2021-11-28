from models.Property import Property


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
