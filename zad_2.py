from datetime import datetime

from zad_1 import Student


class Library:
    def __init__(
            self,
            city: str,
            street: str,
            zip_code: str,
            open_hours: str,
            phone: int) -> None:
        self._city: str = city
        self._street: str = street
        self._zip_code: str = zip_code
        self._open_hours: str = open_hours
        self._phone: int = phone

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value: str) -> None:
        self._street = value

    @property
    def zip_code(self) -> str:
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value: str) -> None:
        self._zip_code = value

    @property
    def open_hours(self) -> str:
        return self._open_hours

    @open_hours.setter
    def open_hours(self, value: str) -> None:
        self._open_hours = value

    @property
    def phone(self) -> int:
        return self._phone

    @phone.setter
    def phone(self, value: int) -> None:
        self._phone = value

    def __str__(self) -> str:
        return f"city: {self._city}, " \
               f"street: {self._street}, " \
               f"zip_code: {self._zip_code}, " \
               f"open_hours: {self._open_hours}, " \
               f"phone: {self._phone}"


class Employee:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 hire_date: datetime,
                 birth_date: datetime,
                 city: str,
                 street: str,
                 zip_code: str,
                 phone: int) -> None:
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._hire_date: datetime = hire_date
        self._birth_date: datetime = birth_date
        self._city: str = city
        self._street: str = street
        self._zip_code: str = zip_code
        self._phone: int = phone

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def hire_date(self) -> datetime:
        return self._hire_date

    @hire_date.setter
    def hire_date(self, value: datetime):
        self._hire_date = value

    @property
    def birth_date(self) -> datetime:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: datetime):
        self._birth_date = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value: str):
        self._street = value

    @property
    def zip_code(self) -> str:
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value: str):
        self._zip_code = value

    @property
    def phone(self) -> int:
        return self._phone

    @phone.setter
    def phone(self, value: int):
        self._phone = value

    def __str__(self) -> str:
        return f"{self._first_name} {self._last_name}, " \
               f"hire_date: {self._hire_date}, " \
               f"birth_date: {self._birth_date}, " \
               f"city: {self._city}, street: {self._street}, " \
               f"zip_code: {self._zip_code}, phone: {self._phone}"


class Order:
    def __init__(self,
                 employee: Employee,
                 student: Student,
                 books: list,
                 order_date: datetime) -> None:
        self._employee: Employee = employee
        self._student: Student = student
        self._books: list = books
        self._order_date: datetime = order_date

    @property
    def employee(self) -> Employee:
        return self._employee

    @employee.setter
    def employee(self, value: Employee):
        self._employee = value

    @property
    def student(self) -> Student:
        return self._student

    @student.setter
    def student(self, value: Student) -> None:
        self._student = value

    @property
    def books(self) -> list:
        return self._books

    @books.setter
    def books(self, value: list) -> None:
        self._books = value

    @property
    def order_date(self) -> datetime:
        return self._order_date

    @order_date.setter
    def order_date(self, value: datetime) -> None:
        self._order_date = value

    def __str__(self) -> str:
        books_str = ""
        for book in self.books:
            books_str += str(book)
        return f"employee: {self.employee},\nstudent: {self.student},\n" \
               f"books: {books_str},\norder_date: {self.order_date}\n "


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


if __name__ == "__main__":
    list_of_libraries = [Library(open_hours=f"{8 + i} - {16 + i}",
                                 city=f"Miasto{i + 1}",
                                 street=f"Ulica{i + 1}",
                                 zip_code=f"0{i}-{i}00",
                                 phone=i)
                         for i in range(2)]
    list_of_books = [Book(library=list_of_libraries[i % 2],
                          author_name=f"Imie{i}",
                          author_surname=f"Naziwsko{i}",
                          publication_date=datetime(2020, 4, 11 + i),
                          number_of_pages=50 + i * 150)
                     for i in range(5)]
    list_of_employees = [Employee(first_name=f"Im{i}",
                                  last_name=f"Naz{i}",
                                  hire_date=datetime(2020, 12, 1 + i),
                                  birth_date=datetime(1990, 3, 10 + i),
                                  city=f"Town{i}",
                                  street=f"Street{i}",
                                  zip_code=f"{i + 1}{i + 1}-{i}0{i + 1}",
                                  phone=i)
                         for i in range(3)]
    list_of_students = [Student(name=f"Student{i}",
                                marks=i * 11) for i in range(3)]
    list_of_orders = [Order(employee=list_of_employees[i],
                            student=list_of_students[i],
                            books=[list_of_books[i]],
                            order_date=datetime(2021, 10, 31))
                      for i in range(2)]

    for order in list_of_orders:
        print(order)
