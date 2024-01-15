# import the os module and module for reading CSV files
import os
import csv

# create the path to collect the data
pypollpath = os.path.join('Resources','election_data.csv')

# Reading using CSV module

with open(pypollpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
with open(pypollpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    row_count = len(list(csvreader))
    
    next(csvreader)
    
    # print(csvreader)
    
    # Read the lines of the file
    lines = csvfile.readlines()
    
    # Create an empty dictionary to store the value counts
    value_counts = {}
    
    # Iterate through each line
    for line in lines:
        
        # split the line into columns
        columns = line.strip().split(',')
        
        # Get the value from the desired column
        value = columns[2]
        
        # Update the value count in the dictionary
        value_counts[value] = value_counts.get(value,0) + 1

    for value, count in value_counts.items():
        percentage = (count / row_count) * 100
        print(f"{value}: {percentage:.3f}%")
        if count == value_counts.max():
            print("Winner:", value)