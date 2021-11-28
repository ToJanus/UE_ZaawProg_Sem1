from models.Property import Property


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
