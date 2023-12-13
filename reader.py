# Import the os and sys modules
import sys
import sqlite3

connection = sqlite3.connect("IMDB_database.db")
crsr = connection.cursor()
print("Connected to IMDB_database.db")

# Akas
file = open("Akas.tsv", "r", encoding="utf-8")
line = ""
print("Loading Akas;")
# Loop through the lines in the file
for line in file:
    # Skip first line
    if line.startswith("titleId"):
        continue
    # Split the line by tab characters
    t = line.split("\t")
    # Append the SQL statement using SQL Parameter in questionmark style
    crsr.execute("INSERT OR IGNORE INTO Akas VALUES (?, ?, ?, ?, ?, ?)", (t[0], t[1], t[2], t[3], t[4], t[7]))

file.close()

# Basics
file = open("Basics.tsv", "r", encoding="utf-8")
line = ""
print("Loading Basics;")
# Loop through the lines in the file
for line in file:
    # Skip first line
    if line.startswith("nconst"):
        continue
    # Split the line by tab characters
    t = line.split("\t")
    # Append the SQL statement using SQL Parameter in questionmark style
    crsr.execute("INSERT OR IGNORE INTO Basics VALUES (?, ?, ?, ?)", (t[0], t[1], t[2], t[3]))

file.close()

# Title_Basics
file = open("Title_Basics.tsv", "r", encoding="utf-8")
line = ""
print("Loading Title_Basics;")
# Loop through the lines in the file
for line in file:
    # Skip first line
    if line.startswith("tconst"):
        continue
    # Split the line by tab characters
    t = line.split("\t")
    # Append the SQL statement using SQL Parameter in questionmark style
    crsr.execute("INSERT OR IGNORE INTO Title_Basics VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7]))

file.close()
# Episode
file = open("Episode.tsv", "r", encoding="utf-8")
line = ""
print("Loading Episode;")
# Loop through the lines in the file
for line in file:
    # Skip first line
    if line.startswith("tconst"):
        continue
    # Split the line by tab characters
    t = line.split("\t")
    # Append the SQL statement using SQL Parameter in questionmark style
    crsr.execute("INSERT OR IGNORE INTO Episode VALUES (?, ?, ?, ?)", (t[0], t[1], t[2], t[3]))

file.close()

# Principals
file = open("Principals.tsv", "r", encoding="utf-8")
line = ""
print("Loading Principals;")
# Loop through the lines in the file
for line in file:
    # Skip first line
    if line.startswith("tconst"):
        continue
    # Split the line by tab characters
    t = line.split("\t")
    # Append the SQL statement using SQL Parameter in questionmark style
    crsr.execute("INSERT OR IGNORE INTO Principals VALUES (?, ?, ?, ?, ?, ?)", (t[0], t[1], t[2], t[3], t[4], t[5]))

file.close()

# Ratings
file = open("Ratings.tsv", "r", encoding="utf-8")
line = ""
print("Loading Ratings;")
# Loop through the lines in the file
for line in file:
    # Skip first line
    if line.startswith("tconst"):
        continue
    # Split the line by tab characters
    t = line.split("\t")
    # Append the SQL statement using SQL Parameter in questionmark style
    crsr.execute("INSERT OR IGNORE INTO Ratings VALUES (?, ?, ?)", (t[0], t[1], t[2]))

# Close the file
file.close()
connection.commit()
print("Done!")
connection.close()





