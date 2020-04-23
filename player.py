from numSlide import *
import pygame


class player():
	def __init__(self, shufNum = 10, mo="None"):
		self.game = numSlide(shufNum)
		self.mo = mo
		#Player passes inputs in to the controller then the controller takes those inputs and sends them

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


	def play(self):
		pygame.time.delay(10)
		run = True
		while run:
			if self.mo == "None":
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							self.move(2)
						if event.key == pygame.K_LEFT:
							self.move(3)
						if event.key == pygame.K_DOWN:
						    self.move(0)
						if event.key == pygame.K_RIGHT:
							self.move(1)
			else:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
				self.move(self.mo.update())



			pygame.display.update()
			
			if self.check():     
				print('Score: ' + str(self.score()))
				break

			self.drawGrid()

		pygame.quit()


		
		



