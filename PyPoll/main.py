import os
import csv
import statistics

csvpath = os.path.join("Resources", "election_data.csv")
outputpath = os.path.join("analysis", "analysis.txt")

totalVotes = 0
mostVotes = 0
mostVotesName = ""
candidateDict = {}
results = ""

# Open csv and store header
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    csvheader = next(csvreader)

    for row in csvreader:

        # Counts total and candidate votes
        # If new candidate, add them to the dict w/ 1 vote
        totalVotes += 1

        if row[2] in candidateDict: candidateDict[row[2]] += 1 

        else: candidateDict[row[2]] = 1

# Stores total votes text at top of results
results += f'Total Votes: {totalVotes}'

# For each candidate, check if they won and add their totals to results
for name, votes in candidateDict.items():

    if votes > mostVotes: 
        mostVotesName = name
        mostVotes = votes

    results += '\n' f'{name}:{votes/totalVotes: 0.3%} ({votes})'

results += '\n' f'Winner: {mostVotesName}'

# Print and Export results
print(results)  

with open(outputpath, "w") as f:
    f.write(results)
        



