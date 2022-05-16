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
file_to_save = os.path.join("resources", "election_analysis.txt")


#initialize a total vote counter
total_votes = 0

#print the candidate name from each row
candidate_options = []
#declare the empty dictionary
candidate_votes= {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
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


#print the candidate name from each row
        candidate_name = row[2]

#if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
#add the candidate name to the candidate list
            candidate_options.append(candidate_name)
#begin tracking that candidate's name
            candidate_votes[candidate_name] = 0
            #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    #save the results to our text file
    with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            #determine winning vote and count and candidate
            # print each candidate's name, vote count and percentage of votes
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # determine if the votes is greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        #print(winning_candidate_summary)
