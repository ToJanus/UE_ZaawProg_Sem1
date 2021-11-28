from datetime import datetime
from decimal import Decimal

from models.KlientBiznesowy import KlientBiznesowy


class Zamowienie:
    def __init__(self,
                 id: int,
                 produkty: list,
                 kl_biznesowy: KlientBiznesowy,
                 utworzono: datetime,
                 prac_obslugujacy: str) -> None:
        self._id: int = id
        self._produkty: list = produkty
        self._kl_biznesowy: KlientBiznesowy = kl_biznesowy
        self._utworzono: datetime = utworzono
        self._prac_obslugujacy: str = prac_obslugujacy

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def produkty(self) -> list:
        return self._produkty

    @produkty.setter
    def produkty(self, value: list) -> None:
        self._produkty = value

    @property
    def kl_biznesowy(self) -> KlientBiznesowy:
        return self._kl_biznesowy

    @kl_biznesowy.setter
    def kl_biznesowy(self, value: KlientBiznesowy) -> None:
        self._kl_biznesowy = value

    @property
    def utworzono(self) -> datetime:
        return self._utworzono

    @utworzono.setter
    def utworzono(self, value: datetime) -> None:
        self._utworzono = value

    @property
    def prac_obslugujacy(self) -> str:
        return self._prac_obslugujacy

    @prac_obslugujacy.setter
    def prac_obslugujacy(self, value: str) -> None:
        self._prac_obslugujacy = value

    def wartosc_zamowienia(self) -> Decimal:
        assert len(self.produkty) > 0, f"Brak produktów"

        suma = 0
        for produkt in self.produkty:
            suma += produkt.cena

        return round(suma, 2)

    def adres_klienta(self) -> str:
        return self.kl_biznesowy.adres

    def __str__(self) -> str:
        produkty_str = ''
        for produkt in self.produkty:
            produkty_str += str(produkt) + '\n'
        return f"Zamowienie:\n" \
               f" O ID: {self.id} złożone przez:\n" \
               f"{self.kl_biznesowy}\n" \
               f"na produkty:\n" \
               f"{produkty_str}\n" \
               f"obsługiwane jest przez {self.prac_obslugujacy}.\n" \
               f"Wartosc zamówienia wynosi {self.wartosc_zamowienia()}\n" \
               f"Adres wysyłki: {self.adres_klienta()}"
