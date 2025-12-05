class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def show(self):
        print("self:",self.x,self.y)
v1=vector(2,3)
v2=vector(4,5)

v3=v1+v2
v3.show()
#Create Vector class. Add __add__ method to add two vectors...explain in bangla