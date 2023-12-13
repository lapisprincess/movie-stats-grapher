#import downloader
#import gzip
#import sqlite3 <- IMPORTANT!
import os
import time
import webbrowser

from globals import *

def main():
    print("Welcome, fellow film buff!")

    datafiles = {}
    for line in open(SCHEMA_PATH, 'r').readlines():
        if '#' not in line:
            info = []
            for word in line.split(', '): info.append(word)
            datafiles.update({info[1]: (info[2], info[0])})

    datafiles.pop("filename")

    check_outdated(datafiles)

    imdb_schema = open(IMDB_SCHEMA_DEFINITION, 'r')


    # CONVERT CSV FILES TO SQL DATABASES




    print("Here are the available relations:")
    for object in datafiles:
        print(" - " + object + ": " + datafiles[object][0])
    print()

    final_table = ""

    prompt = get_input("Are we working with (1) or (2) tables?")

    if int(prompt) != 1: 
        join()
        final_table = "join_results"
    else: 
        final_table = get_input("Please select a table to work with: ")

    try:
        attributes = open(DATA_PATH + final_table, 'r').readline()
        print(attributes)
    except:
        print("Unknown relation! Exiting...")
        exit()

    # graph results






def join():
    # 2 tables joined with common attribute, compare collums r & s
    first = get_input("Please select the first relation: ")
    print("Please select ")

    return False

def get_input(prompt):
    print(prompt)
    return input("> ")



def check_outdated(datafiles):
    outdated = []
    for object in datafiles: 
        path = DATA_PATH + datafiles[object][1]

        c_time = time.gmtime(os.path.getctime(path))

        c_day = c_time.tm_mday
        c_month = c_time.tm_mon
        c_year = c_time.tm_year

        curr_time = time.localtime()
        curr_day = curr_time.tm_mday
        curr_month = curr_time.tm_mon
        curr_year = curr_time.tm_year

        if ((curr_year > c_year) 
        or (curr_month > c_month and c_day > curr_day)):
            outdated.append(object)

    if len(outdated) > 0:
        print("The following data files are outdated by at least a month:")
        print(outdated)
        prompt = input("Update files? (y/n) ")
        if 'y' in prompt: 
            webbrowser.open(IMDB_DATASET_URL) 
            exit(0)





main()