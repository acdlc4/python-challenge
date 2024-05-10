import os
import csv

#Path to collect data form the Resources folder
BudgetData_csv = os.path.join("..","Resources","budget_data.csv")

# Open and read csv
with open(BudgetData_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")

    header = next(budget_reader)
    print(f"Header: {header}")

    for row in budget_reader:
        print(row)

    # date = str(BudgetData_csv[1])
    # print(date)
    # profit = float(budget_reader[1])
    # length = 0
    # length = len(budget_reader)
    totalprofit = 0.00

   
    for monthly in budget_reader:
        totalprofit += float(monthly[1])

    
    print(totalprofit)

