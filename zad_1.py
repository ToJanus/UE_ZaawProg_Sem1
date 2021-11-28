from models.Student import Student

if __name__ == "__main__":
    student1 = Student('Jan', 51)
    student2 = Student('Marek', 50)
    print(student1.is_passed())
    print(student2.is_passed())
