import os
import csv 

# Variables
candidates = []
number_votes = 0
vote_counts= []

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

         #skip the header
    line = next(csvreader,None)

    #go line by line and process each vote
    for line in csvreader:

        #add to total number of votes
        number_votes = number_votes + 1

        #candidate voted for
        candidate = line[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/number_votes*100 
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {number_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}%, ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")  

with open("02-Homework_03-Python_Instructions_PyPoll_Resources_election_data", "w", netline='') as datafile:
	writer = csv.writer(datafile)
writer.writerow("Election Results\n")
writer.writerow("--------------------------\n")
writer.writerow(f"Total Votes: {number_votes}\n")
for count in range(len(candidates)):
    writer.writerow(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
writer.writerow("---------------------------\n")
writer.writerow(f"Winner: {winner}\n")
writer.writerow("---------------------------\n")
