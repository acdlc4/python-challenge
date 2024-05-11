import os
import csv

#Path to collect data form the Resources folder
ElectionData_csv = os.path.join("..","Resources","election_data.csv")
#print(ElectionData_csv)

# Open and read csv
with open(ElectionData_csv) as election_file:
    election_reader = csv.reader(election_file, delimiter=",")
    election_list = list(election_reader)

##create list of all ballots, no header
ballots = [data[0] for data in election_list][1:]

##create list of all counties, no header
counties = [data[1] for data in election_list][1:]


##create list of all candidates, no header
cand_all = [data[2] for data in election_list][1:]

##define total votes
total_votes = len(ballots)

##create unique list of all candidates, alphabetized, no header
cand_short = []
for row in cand_all:
    if row not in cand_short:
        cand_short.append(row)
cand_short.sort(reverse=False)

#count votes by candidate
votes_by_cand = []
i = 0
while i < len(cand_short):
    counter = cand_all.count(cand_short[i])
    votes_by_cand.append(counter)
    i += 1

##calculate winning percentage by candidate
percent_by_cand = []
i = 0
while i < 3:
    percentage = round(votes_by_cand[i] / total_votes *100, 3)
    percent_by_cand.append(percentage)
    i += 1


##create summary list of [candidate name, percentage won, votes won]
summary_list = []
summary_list = [(cand_short[i], percent_by_cand[i], votes_by_cand[i]) for i in range(0, len(cand_short))]
print(summary_list)

##define lookup of and save winner output
winner_lookup = max(votes_by_cand)
winner = summary_list[votes_by_cand.index(winner_lookup)]

##Print output to terminal
print("Election Results\n\n"
    +"-------------------------\n\n"
    +f"Total Votes: {total_votes}\n\n"
    +"-------------------------\n")

i = 0
while i < 3:
    print(f"{cand_short[i]}: "
          +f'{percent_by_cand[i]}% ({votes_by_cand[i]})\n')
    i +=1

print(f"-------------------------\n\n"
      +f"Winner: {winner[0]}\n\n"
      +"-------------------------\n\n")


##Save above output to ElectionResults.txt file, code guidance obtained from  https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
with open('ElectionResults.txt', 'a') as f:
    print(f"Election Results\n\n"
        +"-------------------------\n\n"
        +f"Total Votes: {total_votes}\n\n"
        +"-------------------------\n", file=f)

    i = 0
    while i < 3:
        print(f"{cand_short[i]}: "
            +f'{percent_by_cand[i]}% ({votes_by_cand[i]})\n', file=f)
        i +=1

    print(f"-------------------------\n\n"
        +f"Winner: {winner[0]}\n\n"
        +"-------------------------", file=f)