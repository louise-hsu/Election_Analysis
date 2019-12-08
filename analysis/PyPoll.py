# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
# 1. Initialize a total 
total_votes = 0
# declare a new list- candidate_options
candidate_options = []
# declare an empty dictionary - candidate_votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row.
    headers = next(file_reader)
    #print each row in the csv file.
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
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
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate}: received {vote_percentage:.3}% of the vote.") 
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # write candidate_results in text file
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate

    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# 3. Print the total votes.
#print(total_votes)

# Print the candidate list.
#print(candidate_options)
#print(candidate_votes)