
class Student:
    def __init__(self, name, index_number, marks):
        self.name = name
        self.index_number = index_number
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self):
        return f"Student: {self.name}, nr indeksu: {self.index_number}, średnia ocen: {sum(self.marks)/len(self.marks):.2f}"



student1 = Student("Anna", 12345, [60, 70, 80])
student2 = Student("Kasia", 23456, [30, 40, 50])

print(student1.is_passed())  # True
print(student2.is_passed())  # False

