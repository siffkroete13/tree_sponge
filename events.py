import pygame

from enum import Enum

class EvType(Enum):
    UCI_ENGINE_EV = pygame.USEREVENT + 1
    MENU_EV = pygame.USEREVENT + 2

    
class EvMsg(Enum):
    ENGINE_HUMAN = 1
    HUMAN_ENGINE = 2
    ENGINE_ENGINE = 3
    START_MATCH = 4
