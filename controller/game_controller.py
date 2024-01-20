import pygame
from events import EvType, EvMsg
from view import View
from board import Board
import pygame_menu as pm


class Gamecontroller:
    def __init__(self, num_engines, engine_interfaces):
        self.num_engines = num_engines
        self.engine_interfaces = engine_interfaces

        # Bei allen Schach-Engines Observer registrieren
        for i in range(0, self.num_engines):
            self.engine_interfaces[i].register_observer(self)
        
        self.board = Board()
        
        menu = pm.Menu(title="Main Menu", width = 200, height = 50, theme=pm.themes.THEME_GREEN) 

        # Adding label, selector, button to menu
        menu.add.label(title="Main") 
        menu.add.selector('Set Opponents:', [('Engine-Human', EvMsg.ENGINE_HUMAN),
                                            ('Human-Engine', EvMsg.HUMAN_ENGINE),
                                            ('Engine-Engine', EvMsg.ENGINE_ENGINE)], 
                                            onchange=self.set_opponent)
        menu.add.button('Start Match', self.start_match)
        menu.add.button('Quit', pm.events.EXIT)
        
        self.view = View(menu)
    
    def set_opponent(self, ev_type, ev_message):
        self.trigger_event(ev_type, ev_message) 
        
    def start_match(self):
        self.trigger_event(EvType.MENU_EV, EvMsg.START_MATCH)
        
    def trigger_event(self, ev_type, ev_message):
        """
        Hier kann man auch eigene Events erstellen und in pygame event pipe hinzufügen.
        """
        pygame.event.post(pygame.event.Event(ev_type, message=ev_message))

    def update(self, event):
        """
        Hier kommen alle Events an, die von Pygame, vom User (das ja auch durch pygame geht) und auch 
        die von der Schach-Engine
        """
        return_value = True # True zeigt an, dass das Spiel noch nicht vorbei ist
        
        if event.type == EvType.UCI_ENGINE_EV:
            pass
        elif event.type == EvType.MENU_EV:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
            # Prüfen, ob eine Figur angeklickt wurde
            # Hier sollten Sie die Logik hinzufügen, um zu bestimmen, ob eine Figur ausgewählt wurde
            # Wenn ja, setzen Sie selected_piece und berechnen Sie piece_offset_x und piece_offset_y

        elif event.type == pygame.MOUSEMOTION:
            # Wenn eine Figur ausgewählt ist, aktualisieren Sie ihre Position
            if selected_piece is not None:
                pass
                # Bewegen Sie die Figur basierend auf der Mausposition minus dem Offset

        elif event.type == pygame.MOUSEBUTTONUP:
            # Wenn die Maustaste losgelassen wird, setzen Sie selected_piece zurück
            selected_piece = None
        elif event.type == pygame.QUIT:
            return_value = False
            
        return return_value
            
        
    def start(self):
        """
        Spiel wird gestartet (nicht Schach-Partie sondern das ganze Spiel)
        """
        running = True
        while running:
            for event in pygame.event.get():
                running = self.update(event)
            
            self.view.update(self.board)
            
    def close(self): 
        for i in range(0, self.num_engines):
            self.engine_interface.close()
       
