from typing import List

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"{self.city}, {self.street}, {self.zip_code} (Open: {self.open_hours}, Phone: {self.phone})"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Birth: {self.birth_date}, Hire: {self.hire_date}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.author_name} {self.author_surname}, {self.publication_date}, Pages: {self.number_of_pages}, Library: {self.library.city}"

class Order:
    def __init__(self, employee, student_name: str, books: List[Book], order_date):
        self.employee = employee
        self.student_name = student_name
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)
        return (f"Order Date: {self.order_date}\n"
                f"Employee: {self.employee}\n"
                f"Student: {self.student_name}\n"
                f"Books: {books_str}\n")


library1 = Library("Katowice", "Kościuszki 2", "44-001", "8:00-16:00", "123456789")
library2 = Library("Zabrze", "Łokietka 2", "41-700", "9:00-17:00", "987654321")

employee1 = Employee("Jan", "Nowak", "2021-02-10", "1996-07-01", "Katowice", "Kościuszki 2", "44-001", "123456789")
employee2 = Employee("Małgorzata", "Olejnik", "2020-04-21", "1988-12-11", "Zabrze", "Łokietka 2", "41-700", "987654321")
employee3 = Employee("Patryk", "Kowalski", "2019-08-12", "1990-05-07", "Katowice", "Kościuszki 2", "44-001", "123456789")

student1 = "Kasia"
student2 = "Basia"
student3 = "Asia"

book1 = Book(library2, "2021", "Jan", "King", 249)
book2 = Book(library1, "2020", "Ewa", "Wyspiańska", 180)
book3 = Book(library1, "2019", "Halina", "Kochanowska", 500)
book4 = Book(library1, "2018", "Andrzej", "Piaseczny", 260)
book5 = Book(library2, "2018", "Wiola", "Walaszczyk", 140)

order1 = Order(employee1, student1, [book1, book3, book4], "2025-11-30")
order2 = Order(employee2, student2, [book2, book5], "2025-12-10")

print(order1)
print(order2)
