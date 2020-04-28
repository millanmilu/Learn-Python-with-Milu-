class baseclass:
	pass
class derive(baseclass):
	pass
class rect():
	def __init__(self,w,h):
		self.w = w
		self.h = h
	
	def area(self):
		print(self.w *self.h)	

	def per(self):
		print(  2* self.w +self.h)
	

class square(rect): 
	def __init__(self,h):
		super().__init__(h,h)
		self.h = h

r=rect(12,5)
h = square(12)
r.area()
h.area()
r.per()

