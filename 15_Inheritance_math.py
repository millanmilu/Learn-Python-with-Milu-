class Base :
    def __init__(self,a,b):
        self.a = a
        self.b = b
class addition(Base):
    def __init__(self,a,b):
        print("adding")
        super().__init__(a,b)
        self.c =a +b
        print(self.c)

    def addd(self):
        print(self.a+self.b)
class mul(addition):
    def __init__(self,d,a,b):
        addition.__init__(self,a,b)
        self.d = d
        print(d)
        print(self.a*self.d)
addv =addition(1,5)
addv.addd()
d = mul(4,5,4 )
