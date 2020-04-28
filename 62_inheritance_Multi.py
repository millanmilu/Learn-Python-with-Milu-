class A :
    def a(self):
        print("A = a")
class B :
    def b(self):
        print("B = b")


class C:
    def c(self):
        print("C = c")


class D:
    def d(self):
        print("D = b")

class Derive(A,C):
    pass
class Deriveb(B,D):
    pass



class All(Derive,Deriveb):
    pass
#a = Derive()
#a.a()
#a.c()

b = All()
b.d()

#check subclass
print(issubclass(All,A))
#chekc isinstance
print(isinstance(All,D))