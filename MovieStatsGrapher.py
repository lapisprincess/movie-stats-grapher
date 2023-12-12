
import sqlite3
import matplotlib.pyplot as plt
 
# connecting to the database
connection = sqlite3.connect("MainData.db")
 
# cursor
crsr = connection.cursor()
 
# print statement will execute if there are no errors
print("Connected to the database")

# function that determines how a natural join,
# if any, will be done. Only works for IMDB data.
# See the database schema if there's any confusion.
def tables(table1, table2):
    isBasics = "Basics"
    isPrincipals = "Principals"
    if table1 == table2: # If they're the same, just return the one
        return table1
    if table1 == isBasics: #If this table is Basic, it needs to be joined with Principals
        if table2 != isPrincipals:
            result1 = table1 +" natural join Principals"
            result2 = table2
        else: # If prinicples is already the other table, then don't join yet
            result1 = table1
            result2 = table2
    elif table2 == isBasics: # same as the rules above, but for table 2
        if table1 != isPrincipals:
            result1 = table1
            result2 = "Principals natural join " +table2
        else:
            result1 = table1
            result2 = table2 
    else: #If neither of the two tables are Basic
        result1 = table1
        result2 = table2
    
    return result1 +" natural join " +result2

#Just some print satements to check the above function
print("------------")
print("tables(\"Test\",\"Test\"): " +tables("Test","Test"))
print("tables(\"Basics\",\"Basics\"): " +tables("Basics", "Basics"))
print("tables(\"Principals\",\"Principals\"): " +tables("Principals", "Principals"))
print("tables(\"Basics\",\"Test\"): " +tables("Basics", "Test"))
print("tables(\"Test\",\"Basics\"): " +tables("Test", "Basics"))
print("tables(\"Basics\",\"Principals\"): " +tables("Basics", "Principals"))
print("tables(\"Principals\",\"Basics\"): " +tables("Principals", "Basics"))
print("tables(\"Principals\",\"Test\"): " +tables("Principlas", "Test"))
print("tables(\"Test\",\"Principals\"): " +tables("Test", "Principals"))
print("------------")

#temporary testing variables. Will later be filled in as user inputs
tableA = "Ratings"
tableB = "Ratings"
num = "sum"
r = "averageRating"
s = "numVotes"
table = tables(tableA, tableB)

#The command to get our data in a format we want
sql_command = "select " + r + ", " + num +"(" +s + ") from " +table +" group by " +r +" order by " +r +";"

#The exicution of the above in SQL
crsr.execute(sql_command) 

ans = crsr.fetchall()

#Print statement to see if data is returned properly
for i in ans:
    print(i)

# close the connection
connection.close()


# list of tuples
data = ans

# Extracting data from the tuples
x_values, y_values = zip(*data)

# Creating a graph (works for bar and scatter!)
plt.scatter(x_values, y_values)

# Adding labels and title
plt.xlabel(f'{num}({s})')
plt.ylabel(r)
plt.title(f'{r} vs {num}({s}) for all IMDB Movies')

# Show the plot
plt.show()