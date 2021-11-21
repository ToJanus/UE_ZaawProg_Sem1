class Student:
    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50


student1 = Student('Jan', 51)
student2 = Student('Marek', 50)
print(student1.is_passed())
print(student2.is_passed())
