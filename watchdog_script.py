from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("File modified, restarting script...")
        subprocess.run(["python", "your_exchange_script.py"])

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            observer.join()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()