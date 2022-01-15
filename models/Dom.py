from models.Lokum import Lokum


class Dom(Lokum):
    def __init__(self,
                 cena: float,
                 l_pokoi: int,
                 m2: int,
                 liczba_pieter: int) -> None:
        super().__init__(cena, l_pokoi, m2)
        self._liczba_pieter: int = liczba_pieter

    @property
    def liczba_pieter(self) -> int:
        return self._liczba_pieter

    @liczba_pieter.setter
    def liczba_pieter(self, value: int) -> None:
        self._liczba_pieter = value

    def __str__(self) -> str:
        return f"Dom, dane -> " \
               f"{super().__str__()}, liczba pięter: {self.liczba_pieter}"
