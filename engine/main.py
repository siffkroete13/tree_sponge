import sys

def process_input(command):
    if command == "uci":
        # Identifizieren Sie die Engine
        print("tree_sponce")
        print("Iwan Perepelin")
        # Senden Sie Optionen, falls vorhanden (z.B. Schwierigkeitsgrad)
        # print("option name ... type ... default ...")
        print("uciok")
    elif command == "isready":
        print("readyok")
    elif command == "ucinewgame":
        # Reset der internen Spiellogik für ein neues Spiel
        pass
    elif command.startswith("position"):
        # Verarbeiten Sie die übergebene Position und nachfolgende Züge
        pass
    elif command.startswith("go"):
        # Starten Sie die Zugberechnung
        print("bestmove e2e4")
        pass
    elif command == "quit":
        # Beenden der Engine
        sys.exit(0)

if __name__ == "__main__":
    print("Meine Schach-Engine")
    while True:
        input_line = sys.stdin.readline().strip()
        if input_line == "quit":
            break
        process_input(input_line)