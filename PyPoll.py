# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidtate won
# 5. The winnder of the election based on popular vote.

# Add our dependencies
import datetime
import csv
import os

# Importing csv file by assigning a variable for the file to load the path
file_to_load = '/Users/ivan/Desktop/Bootcamp/Module 3/election-analysis/Resources/election_results.csv'

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader=csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)



