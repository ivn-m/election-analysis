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

#Asssign a variable to save the file path
file_to_save = "/Users/ivan/Desktop/Bootcamp/Module 3/election-analysis/Resources/Analysis/election_analysis.txt"

# Initalize a total vote count
total_votes=0

#Candidate Options
candidate_options=[]
#Declare the empty dictionary
candidate_votes={}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader=csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name=row[2]

        #If the candidate does not match any existing cadnidate...
        if candidate_name not in candidate_options:
            #Add candidate name to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Save the results to our text file.
        with open(file_to_save,"w") as txt_file:

            #Print the final vote count to the terminal
            election_results =(
                f"\nElection Results\n"
                f"-------------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------------\n")

            print(election_results, end="")

            #Save the final vote count to the text file.
            txt_file.write(election_results)

            #Determine the percentage of votes for each candidate by looping through the counts
            # 1. Iterate through the candidate list
            for candidate_name in candidate_votes:
                # 2. Retrieve vote count of candiate
                votes = candidate_votes[candidate_name]
                # 3. Calculate the percentage of votes
                vote_percentage = float(votes) / float(total_votes) * 100

                #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                #Print each candidate, their voter count, and percentage to the terminal
                print(candidate_results)

                #Save the candidate resilts to text file
                txt_file.write(candidate_results)

                #Determine winning vote count and candidate
                #1. Determine if the votes is greater than the winning count
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    #2. If true then set winning_count=votes and winning_percent = vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage
                    #3. Set the winning_canddiate equal to the candidate's name
                    winning_candidate = candidate_name

            winning_candidate_summary =(
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary)

            #Save the winning candidate's name to the text file
            txt_file.write(winning_candidate_summary)
