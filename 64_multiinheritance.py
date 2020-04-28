class Person(object) :
    def __init__(self,name,idnumber):
        self.name = name
        self.Id_num = idnumber
class Employee(object):
    def __init__(self,salary,post):
        self.salary = salary
        self.post = post
class Leader(Person,Employee):
    def __init__(self,name,Id_num,salary,post,points):
        self.points =points
        Person.__init__(self,name,Id_num)
        Employee.__init__(self,salary,post)
        print("Name is " + self.name)
        print("Post is " + self.post)
        print("Id is "+ self.Id_num)
        print("Salary is "+ self.salary)
        print("Points  is "+ self.points)
Name = input("Enter Your Name : ")
Id_num = input("Enter Your Id number : ")
salary = input("Enter Your Salary : ")
post = input("Enter Your Post Name : ")
points = input("Enter Your Points : ")
points =int(points)
ins = Leader(Name,Id_num,salary,post,points)
#ins = Leader('Rahul', "882016", 'Assistant Manager', "75000", "560")
print(type(points))