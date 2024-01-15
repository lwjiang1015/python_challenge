# import the os module and module for reading CSV files
import os
import csv

# create the path to collect the data
pybankpath = os.path.join('Resources','budget_data.csv')

# Reopen the CSV file
with open(pybankpath) as csvfile :
    
    # Create a CSV reader
    csvreader = csv.reader(csvfile)
    
    # Read and store the header row
    csv_header = next(csvreader)
    
    # Count the the total number of months
    row_count = len(list(csvreader))
        
        
# reopen the csvfile
with open(pybankpath) as csvfile:   
    
    csvreader = csv.reader(csvfile)
   
    # skip the header row
    next(csvreader)
    
    # set the initial value for total profit/losses
    total = 0
    for row in csvreader:
        value = int(float(row[1]))
        total += value
    
# Reopen the CSV file
with open(pybankpath) as csvfile :
    
    # Create a CSV reader
    csvreader = csv.reader(csvfile)
    
    # Read and store the header row
    csv_header = next(csvreader)
    
    # Find the index of the column to calculate changes for
    column_index = csv_header.index('Profit/Losses')
    
    # Initialize variables
    previous_value = None
    changes = []
    
    # Iterate over the rows
    for row in csvreader:
        # Get the value of the column
        value = float(row[column_index])
        
        # Calculate the change
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)
        
        # Update the previous value
        previous_value = value
    
# reopen the csvfile
with open(pybankpath) as csvfile :
    
    # Create a CSV reader
    csvreader = csv.reader(csvfile)
    
    # Read and store the header row
    csv_header = next(csvreader)
    
    row_count = len(list(csvreader))
    
    totalchange = int(sum(changes))
    averagechange = round(float(totalchange/(row_count-1)),2)

print("Financial Analysis")
print("------------------------------------")
print("Total Months: ", row_count)
print("Total: ","$",total)
print("Average Change: ", averagechange)

#Open a text file for writing
analysistext = "path_to_output_file.txt" 
with open(analysistext, 'w') as txt_file:
    
    # Write the analysis results to the text file
    txt_file.write("Financial Analysiss\n")
    txt_file.write("-----------------\n")
    txt_file.write("Total Months: {}\n".format(row_count))
    txt_file.write("Total: {}\n".format(total))
    txt_file.write("Average Change: {}\n".format(averagechange))