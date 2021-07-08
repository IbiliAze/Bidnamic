import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.fs_event_handlers import on_created

if __name__ == "__main__":    
    # Set the path format
    path = './monitor' # Any files added to the "monitor" directory will get scanned
    
    # Initialise the event handler
    event_handler = FileSystemEventHandler()

    # Running callback functions
    event_handler.on_created = on_created

    # Create an abserver object
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
