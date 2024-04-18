import os
import csv

# File path
file_name = "Resources/election_data.csv"
file_path = os.path.join(os.getcwd(), file_name)

total_no_votes = 0
number_votes_candidate = []
candidates = []

# Read CSV file
with open('/Users/apple/Desktop/python-challange/PyPall/Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip header
    next(csv_reader)

    for row in csv_reader:
        total_no_votes += 1
        candidate = row[2]  # Assuming candidate's name is in the third column

        # If candidate is new, add to list and initialize votes
        if candidate not in candidates:
            candidates.append(candidate)
            number_votes_candidate.append(1)
        else:
            index = candidates.index(candidate)
            number_votes_candidate[index] += 1

# Calculate percentage of votes for each candidate
percent_votes = [(votes / total_no_votes) * 100 for votes in number_votes_candidate]

# Find the winning candidate
max_votes = max(number_votes_candidate)
winning_index = number_votes_candidate.index(max_votes)
winning_candidate = candidates[winning_index]



# Display results
print("Houston Mayoral Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_no_votes}")
print("-----------------------------------------")
for i in range(len(candidates)): print(f"{candidates[i]}: {percent_votes[i]}% ({number_votes_candidate[i]})")
print(f"Winning Candidate: {winning_candidate}")



# Write to output file
with open("output.txt", "w") as output:
    output.write("Houston Mayoral Election Results\n")
    output.write("--------------------------------------\n")
    output.write(f"Total Votes: {total_no_votes}\n")
    output.write("--------------------------------------\n")
    for i in range(len(candidates)): output.write(f"{candidates[i]}: {percent_votes[i]:.3f}% ({number_votes_candidate[i]})\n")
    output.write("--------------------------------------\n")
    output.write(f"Winner: {winning_candidate}\n")
   
