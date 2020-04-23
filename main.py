from player import *
from model import *
import sys

m1 = model()
p1 = player([256],m1)  # shufNum

pygame.display.set_caption("NumSlide")

p1.play()

print('Original Grid: ' + str(p1.game.origGrid))
print()
print('Shuffle: ' + str(p1.game.shuffle))
print()
print('Player Moves ID: ' + str(p1.game.moves))
print()
print('Player Moves: ' + str(p1.game.movesString))
