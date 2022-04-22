# 1: Print the Total Number of Votes
# 2: Print a list of all candidates who recieved votes
# 3: Count how many times each candidate recieved a vote
# 4: Convert count each candidate recieved a vote into a percentage (# of votes / total number) * 100
# 5: Print the name of the candidate who received the most #s of votes (popular vote)

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file. (If using the open() function without the 'with' keyword, make sure to close() at the end of the code)
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    print(headers)


# Using the open() function with the "w" mode.  
with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    txt_file.write("Counties in the Election")
    txt_file.write("\n ------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    


