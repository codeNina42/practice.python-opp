class fooditem:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def update_price(self, new_price):
        self.price = new_price

    def display(self):
        print("food name:", self.name)
        print("price:", self.price)
        print("calories:", self.calories)


item = fooditem("burger", 150, 200)

item.update_price(180)   # updated to 180

item.display()
