import tkinter as tk
from tkinter import messagebox
# Annahme, dass die Event- und AppState-Klassen entsprechend angepasst wurden.

class Gamecontroller:
    def __init__(self, config_data):
        self.config_data = config_data
        self.app_state = AppState(self.config_data)
        self.root = tk.Tk()
        self.view = View(self.root, self.config_data, self.trigger_event)

    def trigger_event(self, ev_type, ev_message):
        """
        Hier verarbeiten wir die Events direkt, anstatt sie in eine Queue zu stellen.
        """
        if ev_type == 'MENU_EV':
            # Führen Sie entsprechende Aktionen basierend auf ev_message aus
            pass
        # Weitere Event-Typen hier handhaben

    def start(self):
        """
        Initialisiert die GUI und startet die Tkinter mainloop.
        """
        self.view.setup_gui()  # Stellen Sie sicher, dass Ihre View-Klasse eine Methode hat, um die GUI einzurichten
        self.root.mainloop()

    def close(self):
        # Schließen Sie alle Ressourcen, die eine explizite Schließung benötigen
        pass