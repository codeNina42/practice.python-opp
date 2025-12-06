class account:
    def __init__(self,holder):
        self.holder=holder
    def work(self):
         print("Account is working")
    
class SavingsAccount(account):
    def work(self):
        print(f"SavingsAccount of {self.holder} is earning interest")
class CurrentAccount(account):
    def work(self):
        print(f"CurrentAccount of {self.holder} is processing daily transactions")
accounts = [
    SavingsAccount("Sajid"),
    CurrentAccount("Asha"),
    SavingsAccount("Rahim")
]

# Demonstrating polymorphism
for acc in accounts:
    acc.work()