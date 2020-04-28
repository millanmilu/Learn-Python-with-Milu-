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

a = Details()
a.setData(52,"nmdf","gf") 
a.showData()       