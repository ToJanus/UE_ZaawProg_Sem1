class Lokum:
    def __init__(self,
                 cena: float,
                 l_pokoi: int,
                 m2: int) -> None:
        self._cena: int = cena
        self._l_pokoi: int = l_pokoi
        self._m2: int = m2

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, value: float) -> None:
        self._cena = value

    @property
    def l_pokoi(self) -> int:
        return self._l_pokoi

    @l_pokoi.setter
    def l_pokoi(self, value: int) -> None:
        self._l_pokoi = value

    @property
    def m2(self) -> int:
        return self._m2

    @m2.setter
    def m2(self, value: int) -> None:
        self._m2 = value

    def __str__(self) -> str:
        return f"cena: {self.cena} PLN, liczba pokoi: {self.l_pokoi}, " \
               f"liczba metrów kwadratowych: {self.m2}"
