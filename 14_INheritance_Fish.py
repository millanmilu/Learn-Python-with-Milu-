class Fish:
    def __init__(self,first_name,last_name="FIsh",skeleton ="bone"):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton


    def swim(self):
        print("This fish is Swimming")
    def swin_backward(self):
        print("This fish can swim backward")

class Trout(Fish):
    pass
ter = Trout("Terry")
print(ter.last_name)
print(ter.skeleton)
ter.swim()
ter.swin_backward()

