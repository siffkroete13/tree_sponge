from model.board import Board


class AppState:
    NOT_RUNNING = 0
    NEGOTIATION = 1 # Verhandlungen mit UCI
    RUNNING = 2
    PAUSED = 3
    
    def __init__(self, config_data):
        self.config_data = config_data
        self.cur_state = AppState.NOT_RUNNING
        
        self.board = Board()
        
        self.debug_mode = True
        self.verbose_stats = True
        self.max_performance = False
        
        self.last_engine_id = 0
        self.last_uci_command = []
        
    def set_board(self, fen):
        self.board.set_position(fen)
        
    def set_state(self, state):
        self.cur_state = state;
        
    def set_uci_command(self, command, engine_id):
        self.last_uci_command[engine_id] = command
        self.set_state(AppState.NEGOTIATION)