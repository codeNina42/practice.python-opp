class device:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Device Name: {self.name}"
class smartphone(device):
    def __init__(self,name,brand):
        super(). __init__(name)
        self.brand=brand
    def __str__(self):
        return f"Smartphone Name: {self.name} | Brand: {self.brand}"
d1 = device("Laptop")
d2 = device("Tablet")

s1 = smartphone("iPhone 14", "Apple")

items = [d1, d2, s1]
for item in items:
    print(item)