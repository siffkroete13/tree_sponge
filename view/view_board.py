import pygame


class ViewBoard:
    
    def __init__(self):
        self.load_images()

    # Laden der Bilder für Schachfiguren
    def load_images(self):
        pieces = ['b_spawn', 'w_spawn', 'b_knight', 'w_knight', 'b_bishop', 'w_bishop', 'b_rook', 'w_rook', 'b_queen', 'w_queen', 'b_king', 'w_king']
        images = {}
        for piece in pieces:
            images[piece] = pygame.image.load(f'data/imgs/pieces/{piece}.png')
        return images

    # Zeichnen des Schachbretts
    def draw_board(self, window):
        board_img = pygame.image.load('data/imgs/board.png')
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


