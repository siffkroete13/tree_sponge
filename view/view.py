import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from controller.events import EvType, EvMsg, Ev, create_event

class View:
    def __init__(self, config_data, event_callback):
        self.root = tk.Tk()
        self.config_data = config_data
        self.event_callback = event_callback
        
        self.root.geometry("800x600")
        self.root.title("Schachspiel")

        self.init_menu()
        self.load_images()

        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        
        # Bind Mausklick-Ereignis
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        
        # Bind Mausbewegungs-Ereignis
        self.canvas.bind("<Motion>", self.on_mouse_move)
        
        # Bind Maus Loslassen-Ereignis
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

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
        self.event_callback('MENU_EV', 'START_MATCH')
        
    def on_mouse_click(self, event):
        # Event-Handler für Mausklick
        self.event_callback(create_event(EvType.MOUSE_EV, EvMsg.MOUSEBUTTONDOWN, {'x': event.x, 'y': event.y}))

    def on_mouse_move(self, event):
        # Event-Handler für Mausbewegung
        self.event_callback(create_event(EvType.MOUSE_EV, EvMsg.MOUSEMOTION, {'x': event.x, 'y': event.y}))

    def on_mouse_release(self, event):
        # Event-Handler für Maus Loslassen
        self.event_callback(create_event(EvType.MOUSE_EV, EvMsg.MOUSEBUTTONUP, {'x': event.x, 'y': event.y}))
    
    def quit(self):
        self.root.quit()
        self.event_callback(create_event(EvType.MENU_EV, EvMsg.QUIT, {}))
    
    def load_images(self):
        self.images = {}
        for piece in ['b_pawn', 'w_pawn', 'b_knight', 'w_knight', 'b_bishop', 'w_bishop', 'b_rook', 'w_rook', 'b_queen', 'w_queen', 'b_king', 'w_king']:
            path = f"{self.config_data['path_to_pieces']}/{piece}.png"
            image = Image.open(path)
            self.images[piece] = ImageTk.PhotoImage(image)
    
    def draw_board(self, board):
        board_img = Image.open(self.config_data['path_to_board'])
        self.canvas.create_image(0, 0, anchor='nw', image=ImageTk.PhotoImage(board_img))
    
    def draw_pieces(self, board):
        square_size = 800 // 8
        for i in range(64):
            piece = board.piece_at(i)
            if piece:
                x = (i % 8) * square_size
                y = (i // 8) * square_size
                piece_name = f'{piece.color}_{piece.symbol().lower()}'
                self.canvas.create_image(x, y, image=self.images[piece_name], anchor='nw')