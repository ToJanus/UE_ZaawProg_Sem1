from models.Lokum import Lokum


class Mieszkanie(Lokum):
    def __init__(self,
                 cena: float,
                 l_pokoi: int,
                 m2: int,
                 ogrzewanie: str) -> None:
        super().__init__(cena, l_pokoi, m2)
        self._ogrzewanie: str = ogrzewanie

    @property
    def ogrzewanie(self) -> str:
        return self._ogrzewanie

    @ogrzewanie.setter
    def ogrzewanie(self, value: str) -> None:
        self._ogrzewanie = value

    def __str__(self) -> str:
        return f"Mieszkanie, dane -> " \
               f"{super().__str__()}, typ ogrzewania: {self.ogrzewanie}"
