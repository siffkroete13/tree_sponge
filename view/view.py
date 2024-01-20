import pygame
import pygame_menu as pm


class View:
    def __init__(self, menu):
        # Fenstergröße und -einstellungen
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Schachspiel")
        menu.mainloop(self.window) 
       
    def update(self, board):
        board.draw_board()
        board.draw_pieces()
        pygame.display.flip()
  