from datetime import datetime

from models.Book import Book
from models.Employee import Employee
from models.Library import Library
from models.Order import Order
from models.Student import Student

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
