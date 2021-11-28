from datetime import datetime

from models.Library import Library


class Book:
    def __init__(self,
                 library: Library,
                 publication_date: datetime,
                 author_name: str,
                 author_surname: str,
                 number_of_pages: int) -> None:
        self._library: Library = library
        self._publication_date: datetime = publication_date
        self._author_name: str = author_name
        self._author_surname: str = author_surname
        self._number_of_pages: int = number_of_pages

    @property
    def library(self) -> Library:
        return self._library

    @library.setter
    def library(self, value: Library) -> None:
        self._library = value

    @property
    def publication_date(self) -> datetime:
        return self._publication_date

    @publication_date.setter
    def publication_date(self, value: datetime) -> None:
        self._publication_date = value

    @property
    def author_name(self) -> str:
        return self._author_name

    @author_name.setter
    def author_name(self, value: str) -> None:
        self._author_name = value

    @property
    def author_surname(self) -> str:
        return self._author_surname

    @author_surname.setter
    def author_surname(self, value: str) -> None:
        self._author_surname = value

    @property
    def number_of_pages(self) -> int:
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value: int) -> None:
        self._number_of_pages = value

    def __str__(self) -> str:
        return f"library: {self.library}, " \
               f"publication_date: {self.publication_date}, " \
               f"author_name: {self.author_name}, " \
               f"author_surname: {self.author_surname}, " \
               f"number_of_pages: {self.number_of_pages}"
