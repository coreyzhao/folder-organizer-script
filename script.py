import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")
DESTINATION_FOLDER = "/Users/coreyzhao/Desktop/mcgill"
UNKNOWN_DESTINATION_FOLDER = "/Users/coreyzhao/Downloads"

COURSE_CODES = ['comp206', 'comp250', 'comp302', 'math240', 'phys181', 'comp251', 'comp273', 'math208', 'math324']

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        
        if not event.is_directory:
            if os.path.basename(event.src_path).startswith('.'):
                return

            if event.src_path.endswith('.crdownload'):
                self.track_download(event.src_path)
            else:
                self.organize_download(event.src_path)

    def track_download(self, crdownload_path):
        file_path = crdownload_path.replace('.crdownload', '')

        while os.path.exists(crdownload_path):
            time.sleep(2)  

        if os.path.exists(file_path):
            self.organize_download(file_path)

    def organize_download(self, file_path):
        
        if not os.path.exists(file_path):
            return

        course_code = self.extract_course_code_from_filename(file_path)
        course_code = course_code if course_code else "Unsorted"
        
        if course_code != "Unsorted":
            target_folder = os.path.join(DESTINATION_FOLDER, course_code)
        else:
            target_folder = os.path.join(UNKNOWN_DESTINATION_FOLDER)
            
        os.makedirs(target_folder, exist_ok=True)

        new_file_path = os.path.join(target_folder, os.path.basename(file_path))
        shutil.move(file_path, new_file_path)

    def extract_course_code_from_filename(self, file_path):
        file_name = os.path.basename(file_path).lower().replace(' ', '')
        
        for course_code in COURSE_CODES:
            if course_code.lower().replace(' ', '') in file_name:
                return course_code
        
        return None

if __name__ == "__main__":
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
