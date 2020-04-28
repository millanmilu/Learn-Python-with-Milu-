class Person:
	"""docstring for ClassName"""
	def __init__(self,name,age):
		self.name = name
		self.age = age 

	def showname(self):
		print(self.name)
	def showage(self):
		print(self.age)

class student(Person):
	studentId = ""

	def __init__(self,sname,sage,studentId):
		super().__init__(sname,sage)
		self.studentId = studentId

	def getId(self):
		print( self.studentId)

p = Person("Millan",21)

p.showage()
p.showage()

s= student("milu",12,"102")
s.getId()
s.showname()


s1= student("milu",13,"101")
s1.getId()
s1.showname()
s1.showage()