from engine import Search


class ChessEngine:
    def __init__(self):
        self.board = [None] * 144
        self.board_info = None
        
        self.search_engine = Search()
    
    def set_board(self, fen):
        self.board, self.board_info = self.fen_to_array_with_info(fen)
        
    @staticmethod
    def fen_to_array_with_info(fen):
        # Teile die FEN-Zeichenkette in ihre Bestandteile
        parts = fen.split(' ')
        board_part = parts[0]
        active_color = parts[1]
        castling_availability = parts[2]
        en_passant_target = parts[3]
        halfmove_clock = int(parts[4])
        fullmove_number = int(parts[5])

        # Erstelle eine leere Liste für das Schachbrett
        board = []
        
        piece_names = piece_names = {'p':'b_pawn','r':'b_rook','n':'b_knight','b':'b_bishop','q':'b_queen','k':'b_king',
                                    'P':'w_pawn','R':'w_rook','N':'w_knight','B':'w_bishop','Q':'w_queen','K':'w_king'}
        # Fülle das Board-Array basierend auf der FEN-Darstellung
        for row in board_part.split('/'):
            for char in row:
                if char.isdigit():
                    board.extend([None] * int(char))
                else:
                    board.append(piece_names[char])

        # Fülle das board_info-Dictionary
        board_info = {
            'active_color': 'white' if active_color == 'w' else 'black',
            'castling': {
                'white_kingside': 'K' in castling_availability,
                'white_queenside': 'Q' in castling_availability,
                'black_kingside': 'k' in castling_availability,
                'black_queenside': 'q' in castling_availability,
            },
            'en_passant': en_passant_target if en_passant_target != '-' else None,
            'halfmove_clock': halfmove_clock,
            'fullmove_number': fullmove_number
        }

        return board, board_info
    
    def go(self, board):
        best_move = self.search_engine.go()