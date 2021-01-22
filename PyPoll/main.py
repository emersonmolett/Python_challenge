import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
votes =[]
total_candidates = []
candidate_options = []
winner_votes = []
candidate = []
candidate_votes = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    header_row = next(csvreader)

    #read each row of data
    for row in csvreader:

        #add votes
        votes.append(row[0])
        total_candidates = row[0]
        



print('Election Results:')
# calculate total votes
votes = len(votes)
print('Total Votes:')
print(votes)

