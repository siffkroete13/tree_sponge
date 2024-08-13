from controller.events import EvType, EvMsg
from view.view import View
from model.app_state import AppState
from tkinter import messagebox
from engineInterface import EngineInterface



class Gamecontroller:
    def __init__(self, num_engines, config_data):
        self.num_engines = num_engines
        self.config_data = config_data
        self.app_state = AppState(self.config_data)
        self.view = View(self.config_data['view'], self.update)
    
    def init_chess_engines(self):
        self.num_engines = self.config_data.num_engines
        self.engine_interfaces = []
        
        # Bei allen Schach-Engines Observer registrieren
        for i in range(0, self.num_engines):
            self.engine_interfaces[i] = EngineInterface(self.config_data.engine_config.engine_path[i])
            self.engine_interfaces[i].register_observer(self)
   
    def set_opponent(self, event):
       pass
   
    def start_match(self):
        # Match startet, an alle engines Start-Message senden
        for i in range(0, self.num_engines):
            self.engine_interfaces[i].send_command('uci')
            self.app_state.set_uci_command('uci', 0)

    def update(self, event):
        """
        Hier kommen alle Events an von der Engine und vom User (d.h. von View)
        """
        return_value = True # True zeigt an, dass das Spiel noch nicht vorbei ist
        
        if event.type == EvType.UCI_ENGINE_EV:
            if event.msg == 'uciok':
                self.app_state.set_uci_command('uciok', 0)
            print('event: ', event)
        elif EvType.MENU_EV:
            if event.msg == EvMsg.START_MATCH:
                self.start_match()
        elif event.type == EvType.MOUSE_EV:
            # Prüfen, ob eine Figur angeklickt wurde
            # Hier sollten Sie die Logik hinzufügen, um zu bestimmen, ob eine Figur ausgewählt wurde
            # Wenn ja, setzen Sie selected_piece und berechnen Sie piece_offset_x und piece_offset_y
            if event.msg == EvMsg.QUIT:
                return_value = False
            
        return return_value

            
    def close(self): 
        for i in range(0, self.num_engines):
            self.engine_interfaces[i].close()
       
