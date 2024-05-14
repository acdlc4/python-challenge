import os
import csv

##Path to collect data from the Resources folder
ElectionData_csv = os.path.join("..","Resources","election_data.csv")

##Open and read csv
with open(ElectionData_csv) as election_file:
    election_reader = csv.reader(election_file, delimiter=",")
##read and store header row
    election_header = next(election_reader)
##set data as list
    election_list = list(election_reader)

##create list of all ballots, no header
ballots = [data[0] for data in election_list][0:]

##create list of all candidates, no header
cand_all = [data[2] for data in election_list][0:]

##define total votes
total_votes = len(ballots)

##create unique summary list of all candidates, alphabetized, no header
cand_summ = []
for row in cand_all:
    if row not in cand_summ:
        cand_summ.append(row)
cand_summ.sort(reverse=False)

#count votes by candidate
votes_by_cand = []
i = 0
while i < len(cand_summ):
    counter = cand_all.count(cand_summ[i])
    votes_by_cand.append(counter)
    i += 1

##calculate winning percentage by candidate
percent_by_cand = []
i = 0
while i < len(cand_summ):
    percentage = round(votes_by_cand[i] / total_votes *100, 3)
    percent_by_cand.append(percentage)
    i += 1

##create summary list of [candidate name, percentage won, votes won]
summary_list = []
summary_list = [(cand_summ[i], percent_by_cand[i], votes_by_cand[i]) for i in range(0, len(cand_summ))]

##define lookup of and save winner output
winner_lookup = max(votes_by_cand)
winner = summary_list[votes_by_cand.index(winner_lookup)]

##Print output to terminal
print("Election Results\n\n"
    +"-------------------------\n\n"
    +f"Total Votes: {total_votes}\n\n"
    +"-------------------------\n")

i = 0
while i < len(cand_summ):
    print(f"{cand_summ[i]}: "
          +f'{percent_by_cand[i]}% ({votes_by_cand[i]})\n')
    i +=1

print(f"-------------------------\n\n"
      +f"Winner: {winner[0]}\n\n"
      +"-------------------------\n\n")

##check for output directory and create if does not exist
mkdir_path = os.path.join("..","analysis")

if not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

## specify the file to write to 
output_path = os.path.join("..","analysis","ElectionResults.txt")

## open file using "write" mode. specify the variable to hold the contents
with open(output_path, 'w') as writer:
    writer.writelines(["Election Results\n\n"
                       +"-------------------------\n\n"
                       +f"Total Votes: {total_votes}\n\n"
                       +"-------------------------\n\n"])

    i = 0
    while i < len(cand_summ):
        writer.writelines([f"{cand_summ[i]}: "
                           +f'{percent_by_cand[i]}% ({votes_by_cand[i]})\n\n'])
        i +=1

    writer.writelines(["-------------------------\n\n"
                       +f"Winner: {winner[0]}\n\n"
                       +"-------------------------\n\n"])
    
    ##end
