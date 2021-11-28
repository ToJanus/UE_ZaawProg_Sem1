class Klient:
    def __init__(self,
                 id: int,
                 nazwa_klienta: str,
                 adres: str,
                 telefon: str) -> None:
        self._id: int = id
        self._nazwa_klienta: str = nazwa_klienta
        self._adres: str = adres
        self._telefon: str = telefon

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def nazwa_klienta(self) -> str:
        return self._nazwa_klienta

    @nazwa_klienta.setter
    def nazwa_klienta(self, value: str) -> None:
        self._nazwa_klienta = value

    @property
    def adres(self) -> str:
        return self._adres

    @adres.setter
    def adres(self, value: str) -> None:
        self._adres = value

    @property
    def telefon(self) -> str:
        return self._telefon

    @telefon.setter
    def telefon(self, value: str) -> None:
        self._telefon = value

    def __str__(self) -> str:
        return f" {self.nazwa_klienta}, adres: {self.adres}, " \
               f"tel.: {self.telefon}"
