import subprocess
import threading


class EngineInterface:
    def __init__(self, engine_path):
        self.observers = []
        # Starten Sie die Schachengine als separaten Prozess
        self.engine_process = subprocess.Popen(
            ['python', engine_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        self.listener_thread = threading.Thread(target=self.engine_listener, daemon=True)
        self.listener_thread.start()

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def engine_listener(self):
        while True:
            output = self.engine_process.stdout.readline()
            if output == '' and self.engine_process.poll() is not None:
                break
            if output:
                self.notify_observers(output.strip())

    def send_command(self, command):
        self.engine_process.stdin.write(command + "\n")
        self.engine_process.stdin.flush()

  
    def close(self):
        self.engine_process.terminate()