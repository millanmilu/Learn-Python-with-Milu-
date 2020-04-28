"""#__add__ = +
#__sub__
#__mul__
a= "5"
b = "6"
c= 5
d =6
print(a+b)
print(str.__add__(a,b))
print(a+b)
print(int.__add__(c,d))
print(int.__mul__(c,d))
print(int.__sub__(c,d))"""
class Child:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
    def __add__(self, new):
        a1 = self.s1 + new.s2
        a2 = self.s2 + new.s2
        a3 = Child(a1,a2)
        return  a3
    def __gt__(self,new):
        r1 = self.s1 +self.s2
        r2 = new.s1 + new.s2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.s1,self.s2)


c1 = Child(59,53)
c2 = Child(69,53)
c4 = c1+ c2

if c1 > c2:
    print("C1 Wins")
else:
    print("c3 wins")
a = 9
print(a.__str__())
print(c2)