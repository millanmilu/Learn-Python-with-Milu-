class A:
	def __init__(self):
		print("in a Init")
	def f1(self):
		print("f1 is working ")

	def f2(self):
		print("f2 is working")

class B(A):
	def __init__(self):
		super().__init__()
	def f3(self):
		print("f3 is working ")

	def f4(self):
		print("f4 is working")
class C(B):
	def __init__(self):


		print(" init ")
	def f5(self):
		print("f5 is working")		

#a = A()
#a.f1()
b =B()
b.f1()

c =C()
c.f2()