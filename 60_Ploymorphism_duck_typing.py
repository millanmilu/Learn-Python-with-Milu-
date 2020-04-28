class Duck:
    def walk(self):
        print("Duck Walk --thapak thapak ")
    def Run(self):
        print("Suuuuuuuuuu")

class Horse:
    def walk(self):
        print("Horse Walk -tadak tadak")

d = Duck()
h =Horse()

#for animal in (d,h):
 #   animal.walk()
def fun(obj):
    obj.walk()
    obj.Run()
fun(d)
fun(h)