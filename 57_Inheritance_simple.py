class Robot:
    def __init__(self,name):
        self.name =name

    def say_hi(self):
        print("Hi ,i am "+self .name)
class Proboto(Robot):
    pass
x  = Robot("milu")
u = Proboto("millan")
u.say_hi()
x.say_hi()