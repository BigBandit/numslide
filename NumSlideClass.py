# Charlie DeGennaro

import pygame
import pygame.gfxdraw
import random
import time

pygame.init()
screenSquare = 800
win = pygame.display.set_mode([screenSquare, screenSquare])


def copyList(l):
	newL = [[False]*4 for _ in range(4)]
	for i in range(4):
		for j in range(4):
			newL[i][j] = l[i][j]
	return newL


class player():
	def __init__(self):
		self.game = numSlide()


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



class numSlide():
	def __init__(self):
		self.screenSquare = 800
		self.score = 0
		self.isShuffling = True
		self.eX = 3
		self.eY = 3
		self.size = 4
		self.curGrid = [[0]*self.size for _ in range(self.size)]
		self.solved = False
		self.shuffle = []
		self.initGrid()
		self.moves = []
		self.movesString = []
		self.origGrid = copyList(self.curGrid)


	def initGrid(self):
		for i in range(len(self.curGrid)):
			for j in range(len(self.curGrid)):
				self.curGrid[i][j] = 4*i+j+1
		self.shuffleGrid()


	def shuffleGrid(self, shuf = []):
		if len(shuf) == 0:
			for i in range(10):
				self.moveTile(random.randint(0,3))
			for i in range(3):
				self.moveTile(0)
				self.moveTile(1)
		else:
			for i in range(len(shuf)):
				self.moveTile(shuf[i])
			self.shuffle = shuf
		self.isShuffling = False


	def moveTile(self, dir): # 2 is UP, 3 is LEFT, 0 is DOWN, 1 is RIGHT
		if dir == 0 and self.eX != 3:
			self.curGrid[self.eX][self.eY] = self.curGrid[self.eX+1][self.eY]
			self.eX += 1
			if not self.isShuffling:
				self.score += 1
				self.moves.extend([dir])
				self.movesString.extend(['D'])
			else:
				self.shuffle.extend([dir])
		if dir == 1 and self.eY != 3:
			self.curGrid[self.eX][self.eY] = self.curGrid[self.eX][self.eY+1]
			self.eY += 1
			if not self.isShuffling:
				self.score += 1
				self.moves.extend([dir])
				self.movesString.extend(['R'])
			else:
				self.shuffle.extend([dir])
		if dir == 2 and self.eX != 0:
			self.curGrid[self.eX][self.eY] = self.curGrid[self.eX-1][self.eY]
			self.eX -= 1
			if not self.isShuffling:
				self.score += 1
				self.moves.extend([dir])
				self.movesString.extend(['U'])
			else:
				self.shuffle.extend([dir])
		if dir == 3 and self.eY != 0:
			self.curGrid[self.eX][self.eY] = self.curGrid[self.eX][self.eY-1]
			self.eY -= 1
			if not self.isShuffling:
				self.score += 1
				self.moves.extend([dir])
				self.movesString.extend(['L'])
			else:
				self.shuffle.extend([dir])
		self.curGrid[self.eX][self.eY] = 16


	def drawGrid(self):
		for i in range(self.size):
			for j in range(self.size):
				r = pygame.Rect((i*200 ,j*200), (200, 200))
				if self.curGrid[j][i] == 1:
					pygame.draw.rect(win, (255,0,0), r)
				elif self.curGrid[j][i] == 2:
					pygame.draw.rect(win, (200,0,0), r)
				elif self.curGrid[j][i] == 3:
					pygame.draw.rect(win, (150,0,0), r)
				elif self.curGrid[j][i] == 4:
					pygame.draw.rect(win, (100,0,0), r)
				elif self.curGrid[j][i] == 5:
					pygame.draw.rect(win, (0,255,0), r)
				elif self.curGrid[j][i] == 6:
					pygame.draw.rect(win, (0,200,0), r)
				elif self.curGrid[j][i] == 7:
					pygame.draw.rect(win, (0,150,0), r)
				elif self.curGrid[j][i] == 8:
					pygame.draw.rect(win, (0,100,0), r)
				elif self.curGrid[j][i] == 9:
					pygame.draw.rect(win, (0,0,255), r)
				elif self.curGrid[j][i] == 10:
					pygame.draw.rect(win, (0,0,200), r)
				elif self.curGrid[j][i] == 11:
					pygame.draw.rect(win, (0,0,150), r)
				elif self.curGrid[j][i] == 12:
					pygame.draw.rect(win, (0,0,100), r)
				elif self.curGrid[j][i] == 13:
					pygame.draw.rect(win, (255,255,255), r)
				elif self.curGrid[j][i] == 14:
					pygame.draw.rect(win, (200,200,200), r)
				elif self.curGrid[j][i] == 15:
					pygame.draw.rect(win, (100,100,100), r)
				elif self.curGrid[j][i] == 16:
					pygame.draw.rect(win, (0,0,0), r)


	def check(self):
		for i in range(self.size):
			for j in range(self.size):
				if self.curGrid[i][j] != self.size*i+j+1:
					self.solved = False
					return self.solved
		self.solved = True
		return self.solved

p1 = player()

pygame.display.set_caption("NumSlide")

run = True
while run:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				p1.move(2)
			if event.key == pygame.K_LEFT:
				p1.move(3)
			if event.key == pygame.K_DOWN:
			    p1.move(0)
			if event.key == pygame.K_RIGHT:
				p1.move(1)

	# endCount = 0
	# for n in game:
	# 	n.drawGrid()
	# 	if n.check():     
	# 		print('Score: ' + str(n.score))
	# 		endCount += 1
	# 	if endCount == len(game):
	# 		run = False


	p1.drawGrid()
	if p1.check():     
		print('Score: ' + str(p1.score))
		run = False

	pygame.display.update()

print(p1.game.origGrid)
print()
print(p1.game.shuffle)
print()
print(p1.game.moves)
print()
print(p1.game.movesString)

pygame.quit()


