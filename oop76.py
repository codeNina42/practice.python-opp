class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def __eq__(self, other):
        return self.area()==other.area()
r1=rectangle(10,5)
r2=rectangle(10,5)
r3=rectangle(30,6)

print(r1==r2)
print(r2==r3)
