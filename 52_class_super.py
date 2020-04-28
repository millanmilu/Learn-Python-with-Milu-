x = 0
class fruit:
	def __init__(self):
		global x 
		x +=1 
		print("I am a fruit")

class citrus(fruit):
	def __init__(self):
				super().__init__()
				global x 
				x += 2
				print("i am citrus")		
lime = citrus()

print(x)