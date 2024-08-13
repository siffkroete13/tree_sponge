import json
import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from controller.events import EvType, EvMsg, Ev, create_event
from collections import namedtuple

# Definiere das namedtuple
BoardDim = namedtuple('BoardDim', ['x', 'y', 'width', 'height', 'square_width', 'square_height', 'padding_left', 'padding_top'])

class View:
    def __init__(self, config_data, event_callback):
        self.board = []
        
        self.board_dim = None
        self.img_size = {}
        
        self.root = tk.Tk()
        self.config_data = config_data
        self.event_callback = event_callback
        
        self.root.geometry(f"{self.config_data['window_width']}x{self.config_data['window_height']}")

        self.root.title(self.config_data['title'])

        self.init_menu()
        self.load_images()
        
        self.canvas = tk.Canvas(self.root, width=self.config_data['window_width'], height=self.config_data['window_height'])
        self.canvas.pack()
        
        # Bind Mausklick-Ereignis
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        
        # Bind Mausbewegungs-Ereignis
        self.canvas.bind("<Motion>", self.on_mouse_move)
        
        # Bind Maus Loslassen-Ereignis
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)
        
        self.draw_board()
        self.draw_pieces()
        self.draw_ruler()  # Zeichne das Lineal unter dem Schachbrett

        self.root.mainloop()
    
    def init_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Menü Start/Quit
        game_menu = Menu(menubar, tearoff=0)
        game_menu.add_command(label="Start Match", command=self.start_match)
        game_menu.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(label="Game", menu=game_menu)

         # Menü Opponent
        set_opponent_menu = Menu(menubar, tearoff=0)
        set_opponent_menu.add_command(label="Engine-Human", command=lambda: self.set_opponent('Engine-Human'))
        set_opponent_menu.add_command(label="Human-Engine", command=lambda: self.set_opponent('Human-Engine'))
        set_opponent_menu.add_command(label="Engine-Engine", command=lambda: self.set_opponent('Engine-Engine'))
        menubar.add_cascade(label="Set Opponents", menu=set_opponent_menu)
    
    def set_opponent(self, opponent):
        self.event_callback(create_event(EvType.MENU_EV, EvMsg.SET_OPPONENT, opponent))
    
    def start_match(self):
        self.event_callback(create_event(EvType.MENU_EV, EvMsg.START_MATCH))
        
    def on_mouse_click(self, event):
        # Event-Handler für Mausklick
        # self.event_callback(create_event(EvType.MOUSE_EV, EvMsg.MOUSEBUTTONDOWN, {'x': event.x, 'y': event.y}))
        
        # Überprüfe, ob eine Figur an der angeklickten Position ist
        for i in range(len(self.board)):
            piece = self.board[i]
            if piece:
                x = self.board_dim.padding_left + (i % 8) * self.board_dim.square_width
                y = self.board_dim.padding_top + (i // 8) * self.board_dim.square_height

                if x <= event.x <= x + self.board_dim.square_width and y <= event.y <= y + self.board_dim.square_height:
                    self.selected_piece = piece
                    self.selected_piece_image = self.images[piece]
                    self.selected_piece_x = x
                    self.selected_piece_y = y
                    self.piece_offset_x = event.x - x
                    self.piece_offset_y = event.y - y
                    self.canvas.delete("piece_" + str(i))  # Entferne das alte Bild der Figur
                    self.board[i] = None  # Entferne die Figur aus dem Brett-Array
                    break

    def on_mouse_move(self, event):
        # Event-Handler für Mausbewegung
        # self.event_callback(create_event(EvType.MOUSE_EV, EvMsg.MOUSEMOTION, {'x': event.x, 'y': event.y}))
        if self.selected_piece:
            # Bewege die ausgewählte Figur mit der Maus
            self.canvas.delete("moving_piece")  # Lösche das vorherige "bewegte" Bild
            self.canvas.create_image(event.x - self.piece_offset_x, event.y - self.piece_offset_y, image=self.selected_piece_image, anchor='nw', tags="moving_piece")

    def on_mouse_release(self, event):
        # Event-Handler für Maus Loslassen
        # self.event_callback(create_event(EvType.MOUSE_EV, EvMsg.MOUSEBUTTONUP, {'x': event.x, 'y': event.y}))
        
        if self.selected_piece:
            # Berechne das Zielquadrat
            target_col = (event.x - self.board_dim.padding_left) // self.board_dim.square_width
            target_row = (event.y - self.board_dim.padding_top) // self.board_dim.square_height

            # Setze die Figur an die neue Position (auf das Zielquadrat)
            if 0 <= target_col < 8 and 0 <= target_row < 8:
                new_x = self.board_dim.padding_left + target_col * self.board_dim.square_width
                new_y = self.board_dim.padding_top + target_row * self.board_dim.square_height

                self.canvas.create_image(new_x, new_y, image=self.selected_piece_image, anchor='nw', tags="piece_" + str(target_row * 8 + target_col))

            # Lösche die bewegte Figur
            self.canvas.delete("moving_piece")

            # Setze die Auswahl zurück
            self.selected_piece = None
            self.selected_piece_image = None
    
    def quit(self):
        self.root.quit()
        self.event_callback(create_event(EvType.MENU_EV, EvMsg.QUIT, {}))
    
    def load_images(self):
        self.images = {}
        for piece in ['b_pawn', 'w_pawn', 'b_knight', 'w_knight', 'b_bishop', 'w_bishop', 'b_rook', 'w_rook', 'b_queen', 'w_queen', 'b_king', 'w_king']:
            path = f"{self.config_data['path_to_pieces']}/{piece}.png"
            image = Image.open(path)
            
            # Speichere die Größe des Bildes
            self.img_size[piece] = image.size  # (width, height)
        
            self.images[piece] = ImageTk.PhotoImage(image)
    
    def draw_board(self):
        # Zeichne das Schachbrett
        board_img = Image.open(self.config_data['path_to_board'])
        board_img_tk = ImageTk.PhotoImage(board_img)
        
        # Speichere die tatsächlichen Dimensionen des Schachbretts
        padding_top = 19
        padding_left = 17
        self.board_dim = BoardDim(
            x=0,
            y=0,
            width=board_img_tk.width() - (2 * padding_left), 
            height=board_img_tk.height() - (2 * padding_top),
            square_width=70.5,
            square_height=70,
            padding_left=padding_left,
            padding_top=padding_top
        )
    
        self.canvas.create_image(self.board_dim.x, self.board_dim.y, anchor='nw', image=board_img_tk)
        self.canvas.board_img = board_img_tk  # Verhindere, dass das Bild vom Garbage Collector gelöscht wird
    
    def draw_pieces(self):
        # Beispielhafter Aufbau eines Schachbretts mit Figuren
        self.board = [
            "b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook",
            "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn",
            None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None,
            "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn",
            "w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"
        ]
        
        
        for i in range(len(self.board)):
            piece = self.board[i]
            
            if piece:
                # Hol die Bildgröße der Figur
                piece_width, piece_height = self.img_size[piece]
            
                x = self.board_dim.x + self.board_dim.padding_left + ( (i % 8) * self.board_dim.square_width + (self.board_dim.square_width / 2) )
                y = self.board_dim.y + self.board_dim.padding_top + ( (i // 8) * self.board_dim.square_height + (self.board_dim.square_height / 2) )
                self.canvas.create_image(x, y, image=self.images[piece], anchor='center', tags="piece_" + str(i))
                
    def draw_ruler(self):
        square_size = self.board_dim.square_width
        board_width = self.config_data['window_width']
        ruler_y_position = self.board_dim.height + 4  # Position direkt unterhalb des Bretts

        for i in range(30):  # Zeichne 9 Striche (für 8 Quadrate)
            x = i * 20
            self.canvas.create_line(x, ruler_y_position, x, ruler_y_position + 4, fill="black")
            self.canvas.create_text(x, ruler_y_position + 20, text=str(x), anchor='n')

            
            

def mock_update(self, event):
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
                
if __name__ == "__main__":
    config_path = 'config/config.json';

    with open(config_path, 'r') as f:
        config_data = json.load(f)
        view = View(config_data['view'], mock_update)