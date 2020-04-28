class Person:
	species ="Homo sapeience"
	def __init__(self,name,age,color):

		self.name= name	
		self.age = age
		self.color = color
	
	def print(self):
		print("Hello My Name is ",self.name+  self.color)
		print(self.age)
		print(self.color)	


	

		
p = Person("milu",22,"Blue")

p.print()