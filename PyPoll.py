import csv

voter_id = []
county = []
candidate = []
total_vote_counter = 0

unique_candidate = []
candidate_counter = []
candidate_average = []
spot_vote_counter = 0

votes_max = 0
votes_average = 0

#Read in the election CSV File
with open('election_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None) # This line skips reading the Header Row
    for row in readCSV:
    #    voter_id.append(row[0])
        candidate.append(row[2])
        total_vote_counter = total_vote_counter + 1

#Establish list of unique candidates
    for row in candidate: 
    #    check if name in original candidate list
        if row not in unique_candidate: 
            unique_candidate.append(row) 

#Nested For Loop - for each entire unique candidate, scan the entire election and count votes per unique candidate 

for i in range (len(unique_candidate)):
    spot_vote_counter = 0 #Reset spot counter for new unique candidate
    for j in range (len(candidate)):
  
   # Look for unique candidate matches
        if candidate[j] == unique_candidate[i]:
            spot_vote_counter = spot_vote_counter + 1
    candidate_counter.append(spot_vote_counter)

#Calculate averages and winners 

for i in range (len(unique_candidate)):
    candidate_average.append(round(100*(candidate_counter[i] / total_vote_counter)))
    if int(candidate_counter[i]) > votes_max:
        votes_max = int(candidate_counter[i])
        winner = unique_candidate[i]

# Print out results
print("---------------")
print("Total Votes: ", total_vote_counter)
print("---------------")
for i in range (len(unique_candidate)):
    print(unique_candidate[i], " : ",candidate_average[i],"% (",candidate_counter[i],")" )
print("---------------")
print("Winner: ", winner)
print("---------------")