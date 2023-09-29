#Setting up csv import
import os
import csv
#Getting file path (Note: Must be run from main Python-Challenge folder, otherwise it will not find the file)
pollpath =  os.path.join("PyPoll", "Resources", "election_data.csv")
with open(pollpath) as csvfile:
    poll = csv.reader(csvfile, delimiter=',')
    #Declaring lists for later use
    voter = []
    county = []
    candidate = []
    next(poll)
    #Placing data in lists
    for row in poll:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    #Getting total vote counts
    votes = len(voter)
    #Sorting candidate list for use in vote counting
    candidate.sort()
    candidate_count = []
    candidate_votes = []
    #Setting up the first index for vote counting
    first_of_cand = 0
    #Counting votes per candidate
    for x in range(1, len(candidate)):
        if candidate[first_of_cand] != candidate[x]:
            candidate_count.append(candidate[x-1]) 
            candidate_votes.append(x-first_of_cand)
            first_of_cand = x
    #adding in the final candidate and vote count
    candidate_count.append(candidate[len(candidate)-1])
    candidate_votes.append(len(candidate)-first_of_cand)
    #Setting up a list for percent
    percent = []
    #Calculating percent
    for x in range(0, len(candidate_votes)):
        percent.append(candidate_votes[x]/votes*100)
    #Finding the index of the winner
    winner_index = candidate_votes.index(max(candidate_votes))
    #Applying the index to get the name of the winner
    winner = candidate_count[winner_index]
    candidate_string = []
    #Creating the 3 candidate lines to be inserted later
    #This loop cannot be done inside of list definition, and maintains the universality as it still goes from 0 to the length of the list rather than 0 to 2
    for x in range(0,len(percent)):
            candidate_string.insert(0,(candidate_count[x]) + ": " + str(round(percent[x],3)) + "% ("+str(candidate_votes[x])+")")
    #Writing results to text list
    text = ["Election Results","-------------------",
        "Total Votes: "+ str(votes),"-------------------",
        "-------------------",
        "Winner: "+ winner, #chicken dinner
        "-------------------"]
    #Inserting candidate lines in correct spot
    for x in range(len(candidate_string)):
        text.insert(4, candidate_string[x])
    #Printing results
    for x in range(len(text)):
        print(text[x])
#Getting file path
analysis_path = os.path.join("PyPoll", "Analysis", "Analysis.txt")
#Writing text file
with open(analysis_path, 'w') as txt:
    #Leaving the last element out of the for loop avoids an extra page break
    for x in range(0, (len(text)-1)):
        txt.write(text[x] + '\n')
    #The last element is written here instead
    txt.write(text[len(text)-1])
