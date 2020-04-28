class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def pritname(self):
        print(self.name ,self.age)
class child(Person):
#class child:
    def __init__(self,name,age,year):
        """"#if we call Person we have to call self,name,age
        whenever super() called it iherit name,age"""
        #Person.__init__(self,name, age)
        super().__init__(name,age)
        self.year = year
    def welcome(self):
        print(f"Chiild Name is {self.name}\n"
              f"child age is {self.age}\n"
              f"child year is {self.year}".format(self.name,self.age,self.year))

class granchild(child):
    def __init__(self,name,year):
        super().__init__(name,year)
        pass
    def Print(self):
        print(self.name,self.year)



p = Person("Millan",12)
p.pritname()
c = child("Milu",11,2014)
c.pritname()
#print(c.welcome()) for return fun()
c .welcome()

g =granchild("Ilu",2014)
g.Print()