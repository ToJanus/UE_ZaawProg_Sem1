from models.Klient import Klient


class KlientBiznesowy(Klient):
    def __init__(self,
                 id: int,
                 nazwa_klienta: str,
                 adres: str,
                 telefon: str,
                 nip: str) -> None:
        super().__init__(id, nazwa_klienta, adres, telefon)
        self._nip: str = nip

    @property
    def nip(self) -> bool:
        return self._nip

    @nip.setter
    def nip(self, value: bool) -> None:
        self._nip = value

    def __str__(self) -> str:
        return f"KlientBiznesowy:\n" \
               f"{super().__str__()}, NIP: {self.nip}"
