import sys

def process_input(input_str):
    # Verarbeiten Sie die eingehenden UCI-Befehle
    # Senden Sie eine passende Antwort zurück
    print(f"Received: {input_str}")  # Beispielantwort

if __name__ == "__main__":
    while True:
        input_line = sys.stdin.readline().strip()
        if input_line == "quit":
            break
        process_input(input_line)