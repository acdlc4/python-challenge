import os
import csv

##Path to collect data form the Resources folder
BudgetData_csv = os.path.join("..","Resources","budget_data.csv")

##Open and read csv
with open(BudgetData_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
##read and store header row
    budget_header = next(budget_reader)
##set data as list    
    budget_list = list(budget_reader)

##create list of all months, no header
months = [data[0] for data in budget_list][0:]

##create list of all profits, no header
pre_profits = [data[1] for data in budget_list][0:]
profits = [eval(i) for i in pre_profits] ##convert data from strings into numbers

##define the calculation of the summation of all profits
tot_profs = 0
for profit in profits:
    tot_profs += profit

##create list of all differences, no header
diffs = [int(profits[i])-int(profits[i-1]) for i in range(1,len(profits))]

##define the calculation of the summation of all differences as represented by the differences list
tot_diffs = 0.00
for diff in diffs:
    tot_diffs += diff

##define average change to the nearest cent by dividing the summation of all differences divided by the number of items in the differences list
avg_chg = round(tot_diffs / len(diffs),2)

##define max increase/decrease in profits
max_diff = max(diffs)
min_diff = min(diffs)

##index location of max_diff & min_diff in order to return MMM-YY
max_month = months [diffs.index(max_diff) + 1]
min_month = months [diffs.index(min_diff) + 1]


##output to screen terminal
print("Financial Analysis\n\n"
      +"----------------------------\n\n"
      +f"Total Months: {len(months)}\n\n"
      +f"Total: ${tot_profs}\n\n"
      +f"Average Change: ${avg_chg}\n\n"
      +f"Greatest Increase in Profits: {max_month} (${max_diff})\n\n"
      +f"Greatest Decrease in Profits: {min_month} (${min_diff})")


##output to file
##check for output directory and create if does not exist
mkdir_path = os.path.join("..","analysis")

if not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

## specify the file to write to 
output_path = os.path.join("..","analysis","FinReview.txt")

## open file using "write" mode. specify the variable to hold the contents
with open(output_path, 'w') as writer:

    writer.writelines(["Financial Analysis\n\n"
                       +"----------------------------\n\n"
                       +f"Total Months: {len(months)}\n\n"
                       +f"Total: ${tot_profs}\n\n"
                       +f"Average Change: ${avg_chg}\n\n"
                       +f"Greatest Increase in Profits: {max_month} (${max_diff})\n\n"
                       +f"Greatest Decrease in Profits: {min_month} (${min_diff})"])

##end