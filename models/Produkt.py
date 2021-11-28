from decimal import Decimal

from models.Magazyn import Magazyn


class Produkt:
    def __init__(self,
                 nazwa: str,
                 cena: float,
                 kategoria: str,
                 magazyn: Magazyn,
                 ekologiczny: bool) -> None:
        self._nazwa: str = nazwa
        self._cena: Decimal = Decimal(str(cena))
        self._kategoria: str = kategoria
        self._magazyn: Magazyn = magazyn
        self._ekologiczny: bool = ekologiczny

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

    @property
    def cena(self) -> Decimal:
        return self._cena

    @cena.setter
    def cena(self, value: float) -> None:
        self._cena = value

    @property
    def kategoria(self) -> str:
        return self._kategoria

    @kategoria.setter
    def kategoria(self, value: str) -> None:
        self._kategoria = value

    @property
    def magazyn(self) -> Magazyn:
        return self._magazyn

    @magazyn.setter
    def magazyn(self, value: Magazyn) -> None:
        self._magazyn = value

    @property
    def ekologiczny(self) -> bool:
        return self._ekologiczny

    @ekologiczny.setter
    def ekologiczny(self, value: bool) -> None:
        self._ekologiczny = value

    def __str__(self) -> str:
        eko_str = ""
        if self.ekologiczny:
            eko_str = 'ekologiczny'
        else:
            eko_str = 'nieekologiczny'
        return f"Produkt:\n" \
               f" {self.nazwa} w cenie {self.cena}, " \
               f"kategoria {self.kategoria}, " \
               f"{eko_str}"
