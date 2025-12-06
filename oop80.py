class employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print("employee is working")
class developer(employee):
        def work(self):
            print(f"{self.name} is writing code.")
class tester(employee):
        def work(self):
             print(f"{self.name} is testing the software.")
  
employees = [
    developer("Sajid"),
    tester("Asha"),
    developer("Rahim"),
    tester("Karim")
]
for e in employees:
    e.work()