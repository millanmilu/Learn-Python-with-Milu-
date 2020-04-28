import unittest
class Details:
    def __init__(self):
        self.__id = "<No Id>"
        self.__name ="<No Name>"
        self.__gender = "<No Gender>"
    def setData(self,id,name,gender):
        self.__id =id
        self.__name = name
        self.__gender =gender
    def showData(self):
        print("Id   \t\t:",self.__id)
        print("Name \t\t:",self.__name)
        print("Gender\t\t:",self.__gender)
class Employee(Details):
    def __init__(self):
        self.__company ="<No Company>"
        self.__dept = "<No Dept>"
    def setEmployee(self,id,name,gender,comp,dept):
        self.setData(id,name,gender)
        self.__company =comp
        self.__dept = dept
    def showEmployeeData(self):
        self.showData()
        print("Company \t:",self.__company)
        print("Dept \t\t:",self.__dept)


def main():
    e=Employee()
    e.setEmployee(1,"Prem Sharma","Male","New Delhi",110065)
    e.showEmployeeData()

if __name__=="__main__":
    unittest.main()