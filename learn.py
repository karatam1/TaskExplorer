
import csv
from csv import writer
import datetime

def filio(line, command, status):
    with open('hist.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        exists = False
        time = datetime.datetime.now()
        time_str = time.strftime("%x")+"|"+time.strftime("%X")
        for ln in csv_reader:
            if ln[1] == line:
                exists = True   

        if exists == False:
            entry = [command, line, status, time_str]
            add_new_entry('hist.csv', entry)       

def add_new_entry(file_name, entry):
    # Open file in append mode
    write_obj = open(file_name, 'a+', newline='')
    # Create a writer object from csv module
    csv_writer = writer(write_obj)
    # Add contents of list as last row in the csv file
    csv_writer.writerow(entry)


def machL():
    print("This program is a work in progress")
