from models.Developer import Developer


class Zamowienie:
    def __init__(self) -> None:
        self._id_zamowienia: int = None
        self._developer: Developer = None
        self._list_of_lokums: list = None
        self._sposob_platnosci: str = None

    # def __init__(self, id_zamowienia: int,
    #              developer: Developer,
    #              list_of_lokums: list,
    #              sposob_platnosci: str) -> None:
    #     self._id_zamowienia: int = id_zamowienia
    #     self._developer: Developer = developer
    #     self._list_of_lokums: list = list_of_lokums
    #     self._sposob_platnosci: str = sposob_platnosci

    @property
    def id_zamowienia(self) -> int:
        return self._id_zamowienia

    @id_zamowienia.setter
    def id_zamowienia(self, value: int) -> None:
        self._id_zamowienia = value

    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, value: Developer) -> None:
        self._developer = value

    @property
    def list_of_lokums(self) -> list:
        return self._list_of_lokums

    @list_of_lokums.setter
    def list_of_lokums(self, value: list) -> None:
        self._list_of_lokums = value

    @property
    def sposob_platnosci(self) -> str:
        return self._sposob_platnosci

    @sposob_platnosci.setter
    def sposob_platnosci(self, value: str) -> None:
        self._sposob_platnosci = value

    def wartosc_zamowienia(self) -> int:
        sum = 0
        for lokum in self.list_of_lokums:
            sum += lokum.cena

        return round(sum, 2)

    def suma_m2(self) -> int:
        sum = 0
        for lokum in self.list_of_lokums:
            sum += lokum.m2

        return sum

    def __str__(self) -> str:
        lokum_str = ""
        for lokum in self.list_of_lokums:
            lokum_str += "   " + str(lokum) + "\n"
        return f"Zamowienie nr {self.id_zamowienia} " \
               f"będzie wykonywane przez:\n   {self.developer}\n" \
               f"Lista nieruchomości w zamówieniu:\n" \
               f"{lokum_str}" \
               f"Suma metrów kwadratowych nieruchomości z zamówienia: " \
               f"{self.suma_m2()} m^2\n" \
               f"Wartość zamówienia: {self.wartosc_zamowienia()} PLN\n" \
               f"Sposób opłaty zamówienia: {self.sposob_platnosci}"
