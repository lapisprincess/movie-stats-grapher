#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
from collections import defaultdict 

# Read data from the file
with open('TestData.txt', 'r') as file:
    lines = file.readlines()

# Extract column names from the first row
atributes = lines[0].strip().split('\t')

# Extract data from the remaining rows
data = [line.strip().split('\t') for line in lines[1:]]

# Use a defaultdict to accumulate values for each unique value in column 1
averages = defaultdict(list)

for row in data:
    column1_value = row[0]
    column2_value = float(row[1])  # Assuming column 2 contains numeric values
    averages[column1_value].append(column2_value)

# Calculate the average for each unique value in column 1
for key, value in averages.items():
    averages[key] = sum(value) / len(value)

# Separate the data into two lists
column1 = list(averages.keys())
column2 = list(averages.values())

plt.bar(column1, column2)
plt.xlabel(atributes[0])
plt.ylabel(f'Average {atributes[1]}')
plt.title(f'Average {atributes[1]} of each {atributes[0]} for all IMDB Movies')
plt.show()

