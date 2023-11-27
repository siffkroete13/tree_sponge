import pygame

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und -einstellungen
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Schachspiel")

# Schachbrett und Figuren initialisieren
# Hier sollten Sie Ihre Figuren initialisieren, z.B. in einem Dictionary mit Schlüssel als Position und Wert als Figur.

# Variable für die aktuell bewegte Figur
selected_piece = None
piece_offset_x = 0
piece_offset_y = 0

# Laden der Bilder für Schachfiguren
def load_images():
    pieces = ['b_spawn', 'w_spawn', 'b_knight', 'w_knight', 'b_bishop', 'w_bishop', 'b_rook', 'w_rook', 'b_queen', 'w_queen', 'b_king', 'w_king']
    images = {}
    for piece in pieces:
        images[piece] = pygame.image.load(f'C:/Homepage/tree_sponge/data/imgs/pieces/{piece}.png')
    return images

# Zeichnen des Schachbretts
def draw_board(window):
    board_img = pygame.image.load('C:/Homepage/tree_sponge/data/imgs/board.png')
    window.blit(board_img, (0, 0))

# Zeichnen der Schachfiguren
def draw_pieces(window, board, images):
    square_size = 800 // 8  # Größe eines Schachfeldes (angenommen, das Fenster ist 800x800)
    for i in range(64):
        piece = board.piece_at(i)
        if piece:
            x = (i % 8) * square_size
            y = (i // 8) * square_size
            piece_name = f'{piece.color}_{piece.symbol().lower()}'
            window.blit(images[piece_name], (x, y))


def trigger_event(ev_type, ev_payload):
    my_event = pygame.event.Event(ev_type, message=ev_payload)
    pygame.event.post(my_event)
    
    
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
            # Prüfen, ob eine Figur angeklickt wurde
            # Hier sollten Sie die Logik hinzufügen, um zu bestimmen, ob eine Figur ausgewählt wurde
            # Wenn ja, setzen Sie selected_piece und berechnen Sie piece_offset_x und piece_offset_y

        elif event.type == pygame.MOUSEMOTION:
            pass
            # Wenn eine Figur ausgewählt ist, aktualisieren Sie ihre Position
            if selected_piece is not None:
                pass
                # Bewegen Sie die Figur basierend auf der Mausposition minus dem Offset

        elif event.type == pygame.MOUSEBUTTONUP:
            pass
            # Wenn die Maustaste losgelassen wird, setzen Sie selected_piece zurück
            selected_piece = None

    # Zeichnen Sie das Schachbrett und die Figuren
    # Hier sollten Sie Ihren Code zum Zeichnen des Bretts und der Figuren haben

    pygame.display.flip()

pygame.quit()



