class Vehicle:
	def start(self):
		print("starting engine")

	def stop(self):
		print("stopping engine")
class TwoWheeler(Vehicle):
		def	say(self):
				super().start()
				print("i Have two wheels")
				super().stop()

a = TwoWheeler()
a .say()
