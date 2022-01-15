class Developer:
    def __init__(self,
                 nazwa: str,
                 lokalizacja: str,
                 kapital: int,
                 telefon: int) -> None:
        self._nazwa: str = nazwa
        self._lokalizacja: str = lokalizacja
        self._kapital: int = kapital
        self._telefon: int = telefon

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

    @property
    def lokalizacja(self) -> str:
        return self._lokalizacja

    @lokalizacja.setter
    def lokalizacja(self, value: str) -> None:
        self._lokalizacja = value

    @property
    def kapital(self) -> int:
        return self._kapital

    @kapital.setter
    def kapital(self, value: int) -> None:
        self._kapital = value

    @property
    def telefon(self) -> int:
        return self._telefon

    @telefon.setter
    def telefon(self, value: int) -> None:
        self._telefon = value

    def __str__(self) -> str:
        return f"Developer {self.nazwa}, lokalizacja: {self.lokalizacja}, " \
               f"kapitał spółki: {self.kapital} PLN, tel.: {self.telefon}"
