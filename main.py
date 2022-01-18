import os
import csv
import pathlib

#Find the file
csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', 'election_data.csv')

#create variables for recording values
voteCount = 0
candidates = []
voteTotals = []

#vote count is equal to the length of the file minus the header
csvRead = open(csvpath,'r')
voteCount = len(list(csvRead)) - 1

#Gather the full list of candidates
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    next(csvreader, None)

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])

#Gather the number of votes each candidate received
for candidate in candidates:
    sumVotes = 0
    #count all of the lines that contain a vote for them
    with(open(csvpath, "r")) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        #skip the header
        next(csvreader, None)
        for row in csvreader:
            if row[2] == candidate:
                sumVotes = sumVotes + 1
    voteTotals.append(sumVotes)

#Get the highest vote from the arrays
highestVote = 0
indexHighest = 0
index = 0
for i in voteTotals:
    if int(i) > highestVote:
        highestVote = i
        indexHighest = index
    index = index + 1

#output results and write to file
outfile = open(os.path.join(pathlib.Path(__file__).parent.resolve(),'Analysis',"PyPoll_results.txt"),'x')
print("Election Results")
outfile.write("Election Results\n")
print("-------------------------")
outfile.write("-------------------------\n")
print(f"Total Votes: {voteCount}")
outfile.write(f"Total Votes: {voteCount}\n")
print("-------------------------")
outfile.write("-------------------------\n")
#record maximum values
index = 0
maxIndex = 0
maxVotes = 0
for candidate in candidates:
    currAvg = (voteTotals[index]/voteCount)*100
    print(f"{candidates[index]}: {currAvg:.3f}% ({voteTotals[index]})")
    outfile.write(f"{candidates[index]}: {currAvg:.3f}% ({voteTotals[index]})\n")
    #record the current maximums
    if voteTotals[index] > maxVotes:
        maxIndex = index
        maxVotes = voteTotals[index]
    index = index + 1
print("-------------------------")
outfile.write("-------------------------\n")
print(f"Winner: {candidates[maxIndex]}")
outfile.write(f"Winner: {candidates[maxIndex]}\n")
print("-------------------------")
outfile.write("-------------------------\n")