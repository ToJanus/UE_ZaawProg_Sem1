class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name: str = name
        self._marks: int = marks

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value: int) -> None:
        self._marks = value

    def is_passed(self) -> bool:
        return self._marks > 50

    def __str__(self) -> str:
        return f"Student Name: {self._name}, Marks: {self._marks}"
