import os
import csv

#Path to collect data form the Resources folder
BudgetData_csv = os.path.join("..","Resources","budget_data.csv")

def FinancialAnalysis (budgetdata):
    length = len(budgetdata)
    totalprofit = 0.00

    for monthly in budgetdata:
        totalprofit += monthly 

    return totalprofit


print (totalprofit)
print (length)
