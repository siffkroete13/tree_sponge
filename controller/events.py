from enum import Enum

class EvType(Enum):
    UCI_ENGINE_EV = 1
    MENU_EV = 2
    MOUSE_EV = 3


class EvMsg(Enum):
    # Menu Events
    SET_OPPONENT = 1
    START_MATCH = 4
    
    # User Events
    MOUSEBUTTONDOWN = 5
    MOUSEMOTION = 6
    MOUSEBUTTONUP = 7
    QUIT = 8


class Ev:
    def __init__(self, ev_type, ev_msg, ev_payload):
        self.type = ev_type
        self.msg = ev_msg
        self.payload = ev_payload
        

def create_event(ev_type, ev_msg, ev_payload):
    return Ev(ev_type, ev_msg, ev_payload)