import pygame
import config
from game_state import GameState

from game import Game

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("Pokemon Project")

# framerate
clock = pygame.time.Clock()

# from variable imports class Game
game = Game(screen)

game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    pygame.display.flip()