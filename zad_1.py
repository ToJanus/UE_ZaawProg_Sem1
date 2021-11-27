class Student:
    def __init__(self, name: str, marks: int) -> None:
        self.name: str = name
        self.marks: int = marks

    def is_passed(self) -> bool:
        return self.marks > 50

    def __str__(self) -> str:
        return f"Student Name: {self.name}, Marks: {self.marks}"


if __name__ == "__main__":
    student1 = Student('Jan', 51)
    student2 = Student('Marek', 50)
    print(student1.is_passed())
    print(student2.is_passed())
