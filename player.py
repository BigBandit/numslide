from numSlide import *

class player():
	def __init__(self, shufNum = 10):
		self.game = numSlide(shufNum)


	def move(self, dir):
		self.game.moveTile(dir)


	def drawGrid(self):
		self.game.drawGrid()


	def check(self):
		return self.game.check()


	def score(self):
		return self.game.score


	def getGrid(self):
		return self.game.curGrid


	def getWindow(self):
		return self.game.win
