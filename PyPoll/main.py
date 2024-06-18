import os
import csv

election = os.path.join("C:/Users/admin/Desktop/Python-challenge/PyPoll/Resources/election_data.csv")

# open and read the csv file
with open(election, 'r') as file:
    data_election = csv.reader(file, delimiter=",")

  # The total number of votes cast
    next(data_election)
    my_data = list(data_election)
    row_count = len(my_data)

# A complete list of candidates who received votes
    candi_list = list()
    score = list()
    for i in range (0,row_count):
        candidate = my_data[i][2]
        score.append(candidate)
        if candidate not in candi_list: 
            candi_list.append(candidate)
    count = len(candi_list)

  # The percentage and number of votes for each candidate 
    votes = list()
    percentage = list()
    for item in range (0,count):
        names = candi_list[item]
        votes.append(score.count(names))
        value_p = votes[item]/row_count
        percentage.append(value_p)

 # The winner of the election based on popular vote
    won = votes.index(max(votes))   


# export the results into the text file.  
result = "C:/Users/admin/Desktop/Python-challenge/PyPoll/Analysis/election_result.txt"

with open(result, 'w') as file:
    file.write("Election Results\n\n")
    file.write("----------------------------\n\n")
    file.write(f"Total Votes: {row_count}\n\n")
    file.write("----------------------------\n\n")
   
    for k in range (0,count): 
        file.write(f"{candi_list[k]}: {percentage[k]:.3%} ({votes[k]})\n\n")
    file.write("----------------------------\n\n")
    file.write(f"Winner: {candi_list[won]}\n\n")
    file.write("----------------------------\n")