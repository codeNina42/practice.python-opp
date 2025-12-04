class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"Book: {self.title}, Author: {self.author}, Year: {self.year}")
my_book = Book("1984", "George Orwell", 1949)

my_book.describe()
