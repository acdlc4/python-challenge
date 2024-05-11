import os
import csv

##Path to collect data form the Resources folder
BudgetData_csv = os.path.join("..","Resources","budget_data.csv")
print(BudgetData_csv)

##Open and read csv
with open(BudgetData_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")

    budget_list = list(budget_reader)

##create list of all months, no header
months = [data[0] for data in budget_list][1:]

##create list of all profits, no header
pre_profits = [data[1] for data in budget_list][1:]
profits = [eval(i) for i in pre_profits]

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


##Save above output to FinReview.txt file, code guidance obtained from  https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

with open('FinReview.txt', 'a') as f:
    print("Financial Analysis\n\n"
        +"----------------------------\n\n"
        +f"Total Months: {len(months)}\n\n"
        +f"Total: ${tot_profs}\n\n"
        +f"Average Change: ${avg_chg}\n\n"
        +f"Greatest Increase in Profits: {max_month} (${max_diff})\n\n"
        +f"Greatest Decrease in Profits: {min_month} (${min_diff})", file=f)
    