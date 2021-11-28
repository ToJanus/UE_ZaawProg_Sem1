from models.Klient import Klient


class KlientDetaliczny(Klient):
    def __init__(self,
                 id: int,
                 nazwa_klienta: str,
                 adres: str,
                 telefon: str,
                 zdolnosc_kredytowa: bool) -> None:
        super().__init__(id, nazwa_klienta, adres, telefon)
        self._zdolnosc_kredytowa: bool = zdolnosc_kredytowa

    @property
    def zdolnosc_kredytowa(self) -> bool:
        return self._zdolnosc_kredytowa

    @zdolnosc_kredytowa.setter
    def zdolnosc_kredytowa(self, value: bool) -> None:
        self._zdolnosc_kredytowa = value

    def __str__(self) -> str:
        if self.zdolnosc_kredytowa:
            zdolnosc_str = 'ze zdolnością kredytową'
        else:
            zdolnosc_str = 'bez zdolności kredytowej'
        return f"KlientDetaliczny:\n" \
               f"{super().__str__()}, {zdolnosc_str}"
