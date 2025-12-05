# Base class Employee
class Employee:
    def __init__(self, name):
        self.name = name

    # Define how to print the object
    def __str__(self):
        return f"Employee Name: {self.name}"

# Child class Manager that inherits from Employee
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    # Override __str__ to include department
    def __str__(self):
        return f"Manager Name: {self.name} | Department: {self.department}"

# Create objects
employee1 = Employee("Alice")
employee2 = Employee("Bob")
manager1 = Manager("Charlie", "HR")
manager2 = Manager("David", "IT")

# Now you can print the objects directly
print(employee1)  # Output: Employee Name: Alice
print(manager1)   # Output: Manager Name: Charlie | Department: HR
