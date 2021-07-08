import os
import sys
import codecs
import time
import csv
import errno
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def handle_corrupt_file(file_name, csv_file):
    '''
    This function will handle any corruption in a CSV file.
    The checks are as follows:
        - Check for NUL (null) bytes
    '''

    # Check if NUL bytes exist
    if '\0' in open(file_name).read():
        return csv.reader(codecs.open(file_name, 'rU', 'utf-16'), delimiter = '\t')
        # return csv.reader([row.replace('\0', '') for row in csv_file], delimiter = '\t')

    return csv.reader(csv_file, delimiter='\t')


def calculate_roas(row):
    '''
    Function will calculate the ROAS and handle exceptions:
        - ROAS = conversion value/ cost

    If the division fails, 0 will be returned.\n

    '''
    # Get informational values
    roas = 'ROAS'
    search_term = row[0]
    clicks = row[5]
    impressions = row[8]
    conv_value = row[10]
    cost = row[7]

    try:
        # Calculate ROAS
        roas = float(conv_value) / float(cost)
    except Exception as ex:
        roas = 'ROAS'

    return search_term, clicks, impressions, conv_value, roas


def create_file(file_name):
    # assert os.path.isfile(file_name)
    # os.makedirs(os.path.dirname(file_name))
    if not os.path.exists(os.path.dirname(file_name)):
        try:
            os.makedirs(os.path.dirname(file_name))
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise


def write_file(csv_reader, file_name):
    '''
    Write data to an output file
    '''
    # Write to the file
    with open(file_name, 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        # Loop over each line
        for row in csv_reader:
            # Work with full arrays (full data sets)
            if len(row) == 11:
                output_row = calculate_roas(row) # get the ROAS and informational data
                csv_writer.writerow(output_row)


def read_file(file_name):
    with open(file_name, 'r') as csv_file:
        # Get a clean version of the CSV reader by handling file corruption
        csv_reader = handle_corrupt_file(file_name, csv_file)

        # Create the output file
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        dir_name = f'processed/currency/search_terms'
        output_file_name = f'{dir_name}/{timestamp}.csv'
        create_file(output_file_name)

        # Write to the output file
        write_file(csv_reader, output_file_name)


def on_created(event):
    '''
    Callback event handler. The function will be executed by the file system event handler,
    on the "new file created" event. The function will get the full path name of the file and
    pass it as an argument to the "read_file" function
    '''
    file_name = event.src_path
    full_file_name = os.path.dirname(os.path.abspath(__file__)) + '/' + file_name
    read_file(full_file_name)


if __name__ == "__main__":    
    # Set the path format
    path = sys.argv[1] if len(sys.argv) > 1 else './monitor' # current working directory
    
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
