import pygame
import pygame_menu as pm
from controller.events import EvType, EvMsg

class View:
    def __init__(self, config_data, event_callback):
        self.config_data = config_data
        self.event_callback = event_callback
        
        # Fenstergröße und -einstellungen
        self.screen = pygame.display.set_mode((800, 600))  # Setzt die Größe des Fensters
        pygame.display.set_caption("Schachspiel")
        
        self.init_menu()  # Initialisieren Sie das Menü vor der mainloop
        self.load_images()
        
        self.menu.mainloop(self.screen)  # Starten Sie die mainloop nach der Initialisierung des Menüs
        
    
    def init_menu(self):
        self.menu = pm.Menu(title="Main Menu", width=800, height=100, theme=pm.themes.THEME_GREEN)
       
        # Adding label, selector, button to menu
        self.menu.add.label(title="Main")
        self.menu.add.selector('Set Opponents:', [('Engine-Human', EvMsg.ENGINE_HUMAN),
                                            ('Human-Engine', EvMsg.HUMAN_ENGINE),
                                            ('Engine-Engine', EvMsg.ENGINE_ENGINE)], 
                                            onchange=self.set_opponent)
        self.menu.add.button('Start Match', self.start_match)
        self.menu.add.button('Quit', pm.events.EXIT)
       
        
    def set_opponent(self, value, opponent):
        # Hier den Befehl extrahieren, ist es ENGINE_HUMAN oder ENGINE_ENGINE? Oder sonst ein Menü Punkt?
        self.event_callback(EvType.MENU_EV, EvMsg.ENGINE_HUMAN)
        
    def start_match(self, value1, value2):
        self.event_callback(EvType.MENU_EV, EvMsg.START_MATCH)
    
    def update(self, app_state, board):
        self.app_state = app_state
        self.board_data = board
        self.draw_board(board)
        self.draw_pieces(board)
        pygame.display.flip()
  
  
    # Laden der Bilder für Schachfiguren
    def load_images(self):
        self.pieces = ['b_pawn', 'w_pawn', 'b_knight', 'w_knight', 'b_bishop', 'w_bishop', 'b_rook', 'w_rook', 'b_queen', 'w_queen', 'b_king', 'w_king']
        self.images = {}
        for piece in self.pieces:
            self.images[piece] = pygame.image.load(f'{self.config_data['path_to_pieces']}/{piece}.png')

    # Zeichnen des Schachbretts
    def draw_board(self, board):
        board_img = pygame.image.load(self.config_data['path_to_board'])
        self.screen.blit(board_img, (0, 0))

    # Zeichnen der Schachfiguren
    def draw_pieces(self, board):
        square_size = 800 // 8  # Größe eines Schachfeldes (angenommen, das Fenster ist 800x800)
        for i in range(64):
            piece = board.piece_at(i)
            if piece:
                x = (i % 8) * square_size
                y = (i // 8) * square_size
                piece_name = f'{piece.color}_{piece.symbol().lower()}'
                self.screen.blit(self.images[piece_name], (x, y))

