#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the os module and module for reading CSV files
import os
import csv

# create the path to collect the data
pypollpath = os.path.join('Resources','election_data.csv')

# Reading using CSV module

with open(pypollpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row  
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    row_count = len(list(csvreader))
   


# In[2]:


with open(pypollpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row  
    csv_header = next(csvreader)
    
    # skip the header
    next(csvreader)
    
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


# In[3]:


print("Election Results")
print("--------------------")
print("Total Votes: ", row_count)
for value, count in value_counts.items():
    print(f"{value}: {(count/row_count)*100:.3f}%")


# In[6]:


# Open a text file for writing
results_textfile = "path_to_output_file.txt"
with open(results_textfile, 'w') as txt_file:
    
    # Write the analysis results to the text file
    txt_file.write("Election Results\n")
    txt_file.write("-----------------\n")
    txt_file.write("Total Votes: {}\n".format(row_count))
    txt_file.write("-----------------\n")
    
    

