from models.KlientDetaliczny import KlientDetaliczny


class Magazyn:
    def __init__(self,
                 nazwa_magazynu: str,
                 powierzchnia: int,
                 pracownikow: int,
                 miejscowosc: str,
                 kl_detaliczny: KlientDetaliczny) -> None:
        self._nazwa_magazynu: str = nazwa_magazynu
        self._powierzchnia: int = powierzchnia
        self._pracownikow: int = pracownikow
        self._miejscowosc: str = miejscowosc
        self._kl_detaliczny: KlientDetaliczny = kl_detaliczny

    @property
    def nazwa_magazynu(self) -> str:
        return self._nazwa_magazynu

    @nazwa_magazynu.setter
    def nazwa_magazynu(self, value: str) -> None:
        self._nazwa_magazynu = value

    @property
    def powierzchnia(self) -> int:
        return self._powierzchnia

    @powierzchnia.setter
    def powierzchnia(self, value: int) -> None:
        self._powierzchnia = value

    @property
    def pracownikow(self) -> int:
        return self._pracownikow

    @pracownikow.setter
    def pracownikow(self, value: int) -> None:
        self._pracownikow = value

    @property
    def miejscowosc(self) -> str:
        return self._miejscowosc

    @miejscowosc.setter
    def miejscowosc(self, value: str) -> None:
        self._miejscowosc = value

    @property
    def kl_detaliczny(self) -> KlientDetaliczny:
        return self._kl_detaliczny

    @kl_detaliczny.setter
    def kl_detaliczny(self, value: KlientDetaliczny) -> None:
        self._kl_detaliczny = value

    def __str__(self) -> str:
        return f"Magazyn:\n" \
               f" {self.nazwa_magazynu} w miejscowości {self.miejscowosc} " \
               f"o powierzchni {self.powierzchnia} " \
               f"zatrudniający {self.pracownikow} pracownikow"
