class Rocket:
    def __init__(self,name,distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name,self.distance)
class MarsRover(Rocket):
    def __init__(self,name,distance,maker):
        Rocket.__init__(self,name,distance)
        self.maker = maker
    def get_maker(self):
        return  "%s Launched by %s"%(self.name,self.maker)
if __name__ == "__main__":
    x = Rocket("Simple rocket","till Stratosphere")
    y = MarsRover("mars_rover","till mars","ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())



