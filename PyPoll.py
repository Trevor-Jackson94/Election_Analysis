# 1: Print the Total Number of Votes
# 2: Print a list of all candidates who recieved votes
# 3: Count how many times each candidate recieved a vote
# 4: Convert count each candidate recieved a vote into a percentage (# of votes / total number) * 100
# 5: Print the name of the candidate who received the most #s of votes (popular vote)

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter to 0
total_votes = 0

# Candidate options
candidate_options = []

# Declare an empty dictionary for candidates and their vote count
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. (If using the open() function without the 'with' keyword, make sure to close() at the end of the code)
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list IF it's not already in candidate_options
        if candidate_name not in candidate_options:
            
            # Add the candidate name to candidate list
            candidate_options.append(candidate_name)
            
            # Start tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count each time you encounter their name in a row
        candidate_votes[candidate_name] += 1

      
# Calculate each candidate's percentage of votes
# Iterate through the candidate list
for candidate_name in candidate_votes:
    # Retrieve vote count for each candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and their percentage of votes
    print(f'{candidate_name}: Recieved {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage to vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)
    

# Using the open() function with the "w" mode.  
with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    txt_file.write("Counties in the Election")
    txt_file.write("\n ------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    


