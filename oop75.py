class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)

    def __repr__(self):
        return "Book('" + self.title + "', '" + self.author + "', " + str(self.year) + ")"


b1 = Book("Python Basics", "Sajid Ahsan Seyam", 2025)


b1.describe()


print(b1)
