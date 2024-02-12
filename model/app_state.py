class AppState:
    NOT_RUNNING = 0
    RUNNING = 1
    PAUSED = 2
    
    def __init__(self, config_data):
        self.config_data = config_data
        self.cur_state = AppState.NOT_RUNNING
        self.debug_mode = True
        self.verbose_stats = True
        self.max_performance = False
        
