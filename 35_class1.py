class Rectangle:
	def __init__(self,length,breadth,cost = 0):

		self.length = length
		self.breadth = breadth
		self.cost = cost
	def get_area(self):
		return self.length * self.breadth
	def cal_cost(self):
		area = self.get_area()
		return area * self.cost

r = Rectangle(160,120,2000)
print(r.get_area())	
print(r.cal_cost())		