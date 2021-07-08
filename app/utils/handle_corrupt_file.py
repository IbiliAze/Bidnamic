import csv
import io
import codecs

def handle_corrupt_file(file_name, csv_file):
    '''
    This function will handle any corruption in a CSV file.
    The checks are as follows:
        - Check for NUL (null) bytes
    '''

    # Check if NUL bytes exist
    if '\0' in open(file_name).read():
        return csv.reader(codecs.open(file_name, 'rU', 'utf-16'), delimiter = '\t')
        # return csv.reader(io.open(file_name, 'r', encoding='utf-8'), delimiter = '\t')
        # return csv.reader((row.replace('\0','') for row in csv_file), delimiter=",")

    return csv.reader(csv_file, delimiter='\t')