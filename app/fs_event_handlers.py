import os
from app.fs_utils import read_file

def on_created(event):
    '''
    Callback event handler. The function will be executed by the file system event handler,
    on the "new file created" event. The function will get the full path name of the file and
    pass it as an argument to the "read_file" function
    '''
    file_name = event.src_path
    full_file_name = os.path.dirname(os.path.abspath(__file__)) + '/../' + file_name
    read_file(full_file_name)