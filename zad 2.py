class Student:
    def __init__(self, name, index_number, marks):
        self.name = name
        self.index_number = index_number
        self.marks = marks

    def is_passed(self):
        return sum(self.marks)/len(self.marks) > 50

    def __str__(self):
        return f"Student: {self.name}, nr indeksu: {self.index_number}"


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"{self.city}, {self.street}, {self.zip_code} ({self.open_hours}), tel: {self.phone}"


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
        return f"{self.first_name} {self.last_name}, zatrudniony: {self.hire_date}, ur.: {self.birth_date}, {self.street}, {self.zip_code} {self.city}, tel: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.author_name} {self.author_surname}, {self.publication_date}, {self.number_of_pages} stron, dostępna w: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)
        return f"ZAMÓWIENIE ({self.order_date})\n{self.student}\nObsługujący: {self.employee}\nKsiążki:\n{books_str}"


library1 = Library("Warszawa", "Marszałkowska 10", "00-001", "8:00-18:00", "123-456-789")
library2 = Library("Kraków", "Floriańska 5", "30-002", "9:00-17:00", "987-654-321")

employee1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-10", "Warszawa", "Polna 3", "00-100", "111-222-333")
employee2 = Employee("Anna", "Nowak", "2019-03-15", "1988-08-20", "Kraków", "Długa 7", "30-300", "222-333-444")
employee3 = Employee("Piotr", "Zieliński", "2021-06-01", "1995-12-12", "Warszawa", "Krótka 2", "00-200", "333-444-555")

student1 = Student("Alicja", 12345, [60, 75, 80])
student2 = Student("Bartek", 23456, [40, 30, 50])
student3 = Student("Celina", 34567, [55, 65, 70])

book1 = Book(library1, "2015", "Adam", "Mickiewicz", 350)
book2 = Book(library1, "2018", "Henryk", "Sienkiewicz", 420)
book3 = Book(library2, "2020", "Olga", "Tokarczuk", 300)
book4 = Book(library2, "2012", "Bolesław", "Prus", 280)
book5 = Book(library2, "2022", "Andrzej", "Sapkowski", 500)

order1 = Order(employee1, student1, [book1, book2], "2025-01-10")
order2 = Order(employee2, student2, [book3, book4, book5], "2025-01-12")

print(order1)
print("\n" + "="*50 + "\n")
print(order2)

