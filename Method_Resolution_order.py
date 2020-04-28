class A:
	def __init__(self):
		print("a")
		

class B:
	def __init__(self):
		print("b")
		super().__init__()

class X(B) :
	def __init__(self):
		print("xx")
		super().__init__()

class d(A,B):
	"""docstring for d"""
	def __init__(self, arg):
		super(d, self).__init__()
		self.arg = arg
		
		