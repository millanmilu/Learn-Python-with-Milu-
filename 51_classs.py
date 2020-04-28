class Shark:
    def __init__(self,name,last_name,skeleton = "bone",
                eyelids = False):
        self.skeleton = skeleton
        self.eyelids =eyelids
        self.name = name #"milu" #quation
        self.last_name = last_name
        last_name = "macha"

    def swim(self):
        print("This fish is swimming. ")

    def be_awesome(self):
        print(" The Fish  can swim backwrds . ")
        print(self.last_name)


class Trout(Shark):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.last_name = last_name
    def cll(self):
        print(last_name)
def main():
    b = input("Enter The Name : ")
    c = input("Enter last Name :")
    Millan = Shark(b,c)


    Millan.swim()
    Millan.be_awesome()

    #d = input("Enter your Name :")
    #e = input("enter your last name :")
    #child = Shark(d,e)
    #print(child.name + " "+ child.last_name )
    # print(child.skeleton)
    # print(child.eyelids)
    # child.swim()
    # child.be_awesome()
    ch = Trout("Milu",4)
    ch.swim()



if __name__== "__main__":
    main()
