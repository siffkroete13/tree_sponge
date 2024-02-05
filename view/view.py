import pygame
import pygame_menu as pm
from controller.events import EvType, EvMsg

class View:
    def __init__(self, menu):
        self.menu = pm.Menu(title="Main Menu", width = 200, height = 50, theme=pm.themes.THEME_GREEN) 

        # Adding label, selector, button to menu
        self.menu.add.label(title="Main") 
        self.menu.add.selector('Set Opponents:', [('Engine-Human', EvMsg.ENGINE_HUMAN),
                                            ('Human-Engine', EvMsg.HUMAN_ENGINE),
                                            ('Engine-Engine', EvMsg.ENGINE_ENGINE)], 
                                            onchange=self.set_opponent)
        self.menu.add.button('Start Match', self.start_match)
        self.menu.add.button('Quit', pm.events.EXIT)
        
        # Fenstergröße und -einstellungen
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Schachspiel")
        menu.mainloop(self.window) 
    
    def init_menu(self):
        pass
    
    
    def update(self, board):
        board.draw_board()
        board.draw_pieces()
        pygame.display.flip()
  