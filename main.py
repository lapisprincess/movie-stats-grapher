import os                   # get file info
import time                 # check time to see if files are outdated
import webbrowser           # open web pages
import sqlite3              # used to check if databases were empty

#import gzip                # potentially unzip files?

import reader as reader     # Branson's code
import MovieStatsGrapher    # Riley's code

from globals import *       # global variales

def main():
    print("Welcome, fellow film buff!")
    bless()

    # determine if we're working with the lite or full version
    print("Are we working with the (f)ull IMDb dataset,")
    print("or are we just working with the (l)ite files?")
    if 'f' in input("> "): path = DATA_PATH
    else: path = DATA_PATH_LITE

    # get available tables, check if any are outdated
    datafiles = {}
    for line in open(SCHEMA_PATH, 'r').readlines():
        if '#' not in line:
            info = []
            for word in line.split(', '): info.append(word)
            datafiles.update({info[1]: (info[2], info[0])})
    datafiles.pop("filename")
    try: check_outdated(datafiles, path)
    except:
        print("It seems like not all TSV files are available!")
        print("Please refer to the README for installing files to work with :)")
        exit(0)

    # check if we need to run Branson's reader and initialize the db
    def database_uninitialized():
        print("It seems like the database hasn't been initialized!")
        print("Convert tsv's to database? (y/n)")
        print("This could take a while if using full dataset!") 
        if 'y' == input("> "): reader.convert_tsv_to_db()
        else: exit(0)

    os.chdir(path)
    if "IMDB_database.db" not in os.listdir(): 
        print("database doesn't exist!")
        database_uninitialized()

    try:
        connect = sqlite3.connect("IMDB_database.db")
        cursor = connect.cursor()
        for attribute in datafiles:
            cursor.execute("SELECT * FROM " + attribute)
            if len(cursor.fetchall()) == 0:
                print("database is empty!")
                database_uninitialized()
    except:
        print("database is missing attributes!")
        database_uninitialized()

    print("Here are the available relations:")
    for object in datafiles:
        print(" - " + object + ": " + datafiles[object][0])
    print()

    running = True
    while running:
        tableA = input("First relation: ")
        tableB = input("Second relation: ")
        print("Attributes in " + tableA + ":")
        attributesA = open(tableA + ".tsv", 'r').readline().split("\t")
        attributesA[len(attributesA)-1] = attributesA[len(attributesA)-1][:-2]
        print(attributesA)
        print()
        print("Attributes in " + tableB + ":")
        attributesB = open(tableB + ".tsv", 'r').readline().split("\t")
        print(attributesB)
        print()
        common = False
        for attr in attributesA:
            if attr in attributesB: common = True
        if not common: 
            print("No common attributes! Exiting...")
            exit(0)
        r = input("Attribute x: ")
        s = input("Attribute y: ")
        available_groupings = ["", "sum", "avg", "max", "min", "count"]
        print("Functions that can be applied to y:" + str(available_groupings))
        print("(Leave blank for no function)")
        num = input("Function to apply to y: ")
        if num in available_groupings:
            MovieStatsGrapher.graph_data(tableA, tableB, num, r, s)
        else: print("Not an available grouping method!")
        running = False


def check_outdated(datafiles, data_path):
    outdated = []
    for object in datafiles: 
        path = data_path + datafiles[object][1]

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

def bless():
    username = os.path.expanduser("~")
    username = username[username.index("/", 1)+1:]
    print()
    print("                           /~\   May the force be with you, " + username + "!")
    print("                          (O O) _/")
    print("                          _\=/_")
    print("          ___            /  _  \\")
    print("         / ()\          //|/.\|\\\\")                       
    print("       _|_____|_       ||  \_/  ||")
    print("      | | === | |      || |\ /| ||")
    print("      |_|  O  |_|       # \_ _/ #")
    print("       ||  O  ||          | | |")
    print("       ||__*__||          | | |")
    print("      |~ \___/ ~|         []|[]")
    print("      /=\ /=\ /=\         | | |")
    print("______[_]_[_]_[_]________/_]_[_\_____")
    print()

main() # run it all >:3