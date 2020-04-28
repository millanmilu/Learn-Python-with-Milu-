class cat :
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make(self):
        print("Meow")
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make(self):
        print("Bark")
#def fun(object):
 #   object.info()
cat1 = cat("Milu",12)
dog1 = dog("Millan",13)
#fun(cat1)
#fun(dog1)

for a in (cat1,dog1):
    a.info()
    a.make()