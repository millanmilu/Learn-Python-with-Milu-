class cal:
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def Summation(self,a,b):
            return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
class Derived(cal,Calculation2):
    def Divide(self,a,b):
        return a/b
c =cal(12,5)
d = Derived(12,4)
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))