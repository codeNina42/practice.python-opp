class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def describe(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Create an object of Student
s1 = Student("Sajid", 20, "A")

# Call the describe method
s1.describe()
