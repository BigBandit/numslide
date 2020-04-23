from player import *

<<<<<<< HEAD
p1 = player(10)  # shufNum


pygame.display.set_caption("NumSlide")

=======
p1 = player([10])  # shufNum

pygame.display.set_caption("NumSlide")

playerInControl = True

>>>>>>> 55442efeb516725dcd7e4c76ceba67b527104d83

run = True
while run:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
<<<<<<< HEAD
		if event.type == pygame.KEYDOWN:
=======
		if event.type == pygame.KEYDOWN and playerInControl:
>>>>>>> 55442efeb516725dcd7e4c76ceba67b527104d83
			if event.key == pygame.K_UP:
				p1.move(2)
			if event.key == pygame.K_LEFT:
				p1.move(3)
			if event.key == pygame.K_DOWN:
			    p1.move(0)
			if event.key == pygame.K_RIGHT:
				p1.move(1)

	p1.drawGrid()
	if p1.check():     
		print('Score: ' + str(p1.score()))
		run = False

	pygame.display.update()

pygame.quit()

print('Original Grid: ' + str(p1.game.origGrid))
print()
print('Shuffle: ' + str(p1.game.shuffle))
print()
print('Player Moves ID: ' + str(p1.game.moves))
print()
print('Player Moves: ' + str(p1.game.movesString))
