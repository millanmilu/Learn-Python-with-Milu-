class person:
	def __init__(self,fname,lname):
		self.fname = fname
		self.lname = lname

	def printname(self):
		print(self.fname +""+self.lname)

class student(person):
	def __init__(self,fname,lname,year):
		super(student,self).__init__(fname,lname)
		self.year = year


	def Welcome(self):
		print("welcome",self.fname,self.lname,"To the class of ",self.year)

a = student("milu","Das","2015")
a.Welcome()			
