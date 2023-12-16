import os
import sys

# little program I wrote up to shorten every tsv in the lite folder
# max_lines determines the maximum number of lines for each file
def shorten_files(max_lines):
    # if we're working from root, we need to adjust path
    if os.getcwd != "lite_data": os.chdir("lite_data") 
    for file in os.listdir():
        if ".tsv" in file:
            curr_line = 0
            relevant_data = []
            # start by reading file without going past max_lines
            f = open(file, 'r')
            line = f.readline()
            while line != None and curr_line < max_lines:
                relevant_data.append(line)
                line = f.readline()
                curr_line += 1
            # write relevant lines to file
            f = open(file, 'w')
            for line in relevant_data: f.write(line)
            f.close()

if len(sys.argv) == 1: shorten_files(100)
else: shorten_files(int(sys.argv[1]))