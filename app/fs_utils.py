import os
import time
import errno
import csv
from app.utils.handle_corrupt_file import handle_corrupt_file
from app.utils.calculate_roas import calculate_roas

def read_file(file_name):
    '''
    Read the CSV file. Output file will be created and processed data will be appended to it
    '''
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


def create_file(file_name):
    '''
    To create a file:
        - Check if file exists
        - If not, create it
    '''
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