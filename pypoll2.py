#Add Dependencies
import csv
import os
# csvpath = os.path.join("resources/election_results.csv")

# #with open(csvpath) as csvfile:
#    #csvreader = csv reader(csvfile, delimiter = ',')

#     #for row in csvreader:
# file_to_load = 'resources/election_results.csv'

#safer way to open file
# with open(file_to_load) as election_data:
#     print(election_data)

#manually open/close file
# election_data = open(file_to_load, 'r')
# election_data.close()

#dir(os)
#Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
#Assign a variable to save the file
file_to_save = os.path.join("analysis", "election_analysis.txt")


#initialize a total vote counter
total_votes = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# open(file_to_load, "w")
#safer way to open file
# with open(file_to_load) as election_data:
#     print(election_data)

#use the open statement to open the file as a text file
# outfile = open(file_to_load, "w")

# #write some data to the file
# outfile.write("Hello World")

# #close the file
# outfile.close()

# Read the file object with the reader function
    #file_reader = csv.reader(election_data)

#Read the header row
    headers = next(file_reader)

#Print each row in the CSV file
    for row in file_reader:
        total_votes = total_votes + 1


#print the total votes
print(total_votes)

   # headers = next(file_reader)
    #print(headers)
