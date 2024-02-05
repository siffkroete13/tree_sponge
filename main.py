import json
import pygame
from controller.game_controller import Gamecontroller
from engineInterface import EngineInterface

# Initialisierung von Pygame
pygame.init()

engine_interface_1 = EngineInterface('engine/main.py')
# engine_interface_2 = EngineInterface('eingine/main.py')

config_path = 'config/config.json';

with open(config_path, 'r') as f:
        config_data = json.load(f)
        
game_controller = Gamecontroller(1, config_data)

game_controller.start()

pygame.quit()
