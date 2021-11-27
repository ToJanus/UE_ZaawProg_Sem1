from datetime import datetime

from zad_1 import Student


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: int) -> None:
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.open_hours: str = open_hours
        self.phone: int = phone

    def __str__(self) -> str:
        return f"city: {self.city}, street: {self.street}, zip_code: {self.zip_code}, open_hours: {self.open_hours}, " \
               f"phone: {self.phone}"


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
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.hire_date: datetime = hire_date
        self.birth_date: datetime = birth_date
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.phone: int = phone

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, hire_date: {self.hire_date}, birth_date: {self.birth_date}, " \
               f"city: {self.city}, street: {self.street}, zip_code: {self.zip_code}, phone: {self.phone}"


class Order:
    def __init__(self, 
                employee: Employee, 
                student: Student, 
                books: list, 
                order_date: datetime) -> None:
        self.employee: Employee = employee
        self.student: Student = student
        self.books: list = books
        self.order_date: datetime = order_date

    def __str__(self) -> str:
        books_str = ""
        for book in self.books:
            books_str += str(book)
        return f"employee: {self.employee},\nstudent: {self.student},\nbooks: {books_str},\norder_date: {self.order_date}\n"


class Book:
    def __init__(self,
                 library: Library,
                 publication_date: datetime,
                 author_name: str,
                 author_surname: str,
                 number_of_pages: int) -> None:
        self.library: Library = library
        self.publication_date: datetime = publication_date
        self.author_name: str = author_name
        self.author_surname: str = author_surname
        self.number_of_pages: int = number_of_pages

    def __str__(self) -> str:
        return f"library: {self.library}, publication_date: {self.publication_date}, author_name: {self.author_name}, " \
               f"author_surname: {self.author_surname}, number_of_pages: {self.number_of_pages}"


if __name__ == "__main__":
    list_of_libraries = [Library(open_hours=f"{8+i} - {16+i}",
                                city=f"Miasto{i+1}",
                                street=f"Ulica{i+1}",
                                zip_code=f"0{i}-{i}00",
                                phone=i)
                        for i in range(2)]
    list_of_books = [Book(library=list_of_libraries[i%2],
                        author_name=f"Imie{i}",
                        author_surname=f"Naziwsko{i}",
                        publication_date=datetime(2020, 4, 11+i),
                        number_of_pages=50 + i * 150)
                    for i in range(5)]
    list_of_employees = [Employee(first_name=f"Im{i}",
                                last_name=f"Naz{i}",
                                hire_date=datetime(2020, 12, 1+i),
                                birth_date=datetime(1990, 3, 10+i),
                                city=f"Town{i}",
                                street=f"Street{i}",
                                zip_code=f"{i+1}{i+1}-{i}0{i+1}",
                                phone=i) for i in range(3)]
    list_of_students = [Student(name=f"Student{i}",
                                marks=i*11) for i in range(3)]
    list_of_orders = [Order(employee=list_of_employees[i],
                            student=list_of_students[i],
                            books=[list_of_books[i]],
                            order_date=datetime(2021, 10, 31)) for i in range(2)]

    for order in list_of_orders:
        print(order)
