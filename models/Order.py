from datetime import datetime

from models.Employee import Employee
from models.Student import Student


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
