class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __sub__(self,other  ):
        return vector(self.x-other.x,self.y-other.y)
    def show(self):
        print("vector",self.x,self.y)

v1=vector(5,4)
v2=vector(2,1)
v3=v1-v2
v3.show()
