class Point:
    def reset(self): #self -Parameter
        self.x = 0
        self.y = 0
"""The self argument to a method is simply a reference to the object that the method
is being invoked on. We can access attributes and methods of that object as if it were
any another object. This is exactly what we do inside the reset method when we set
the x and y attributes of the self object."""
p = Point()
p.reset()
print(p.x,p.y)
