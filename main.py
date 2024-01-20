import pygame
from game_controller import Gamecontroller
from engineInterface import EngineInterface

# Initialisierung von Pygame
pygame.init()

engine_interface_1 = EngineInterface('engine/main.py')
# engine_interface_2 = EngineInterface('eingine/main.py')

game_controller = Gamecontroller(1, [engine_interface_1])

game_controller.start()

pygame.quit()
