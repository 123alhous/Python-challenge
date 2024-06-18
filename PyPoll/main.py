# Import Libraries os and csv
import os
import csv

election = os.path.join("C:/Users/admin/Desktop/Python-challenge/PyPoll/Resources/election_data.csv")


with open(election, 'r') as file:
    data_election = csv.reader(file, delimiter=",")

  # The total number of votes cast (row count after the header)
    next(data_election)
    data = list(data_election)
    row_count = len(data)

  # Create new list from CSV column "C" to get a complete list of candidates who received votes
    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
    candicount = len(candilist)

  # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # The winner of the election based on popular vote.
    winner = votes.index(max(votes))   

  
result = "C:/Users/admin/Desktop/Python-challenge/PyPoll/Analysis/election_result.txt"

with open(result, 'w') as file:
    file.write("Election Results\n\n")
    file.write("----------------------------\n\n")
    file.write(f"Total Votes: {row_count}\n\n")
    file.write("----------------------------\n\n")
   
    for k in range (0,candicount): 
        file.write(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]})\n\n")
    file.write("----------------------------\n\n")
    file.write(f"Winner: {candilist[winner]}\n\n")
    file.write("----------------------------\n")