class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = Student("Kasia", [20, 80, 80])
student2 = Student("Krzysztof", [40, 50, 20])

print(student1.is_passed())
print(student2.is_passed())
