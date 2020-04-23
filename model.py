import random

class model:

	def __init__(self, behavior="random"):
		self.behavior = behavior.lower()


	def behave(self):
		if(self.behavior == "random"):
			return random.randint(0,3)


	def update(self):
		return self.behave()

