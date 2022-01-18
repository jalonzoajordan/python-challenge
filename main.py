import os
import csv
import pathlib

#Find the file
csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', 'budget_data.csv')

#create variables for recording values
months = []
sumProfits = 0.00
avgProfits = 0.00
highProfMonth = "ERROR - NOT FOUND"
highProfit = 0.00
lowProfMonth = "ERROR - NOT FOUND"
lowProfit = 0.00

#calculate for each row
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    next(csvreader, None)

    for row in csvreader:
        currAmt = float(row[1])
        if row[0] not in months:
            months.append(row[0])
        sumProfits = sumProfits + currAmt
        if currAmt > float(highProfit):
            highProfMonth = row[0]
            highProfit = currAmt
        if currAmt < float(lowProfit):
            lowProfMonth = row[0]
            lowProfit = currAmt
avgProfits = sumProfits/len(months)

#Output Results
print("Financial Analysis")
print("  ---------------------------- ")
print(f"Total Months: {len(months)}")
print(f"Total: {sumProfits:.2f}")
print(f"Average Change: {avgProfits:.2f}")
print(f"Greatest Increase in Profits: {highProfMonth} ({highProfit:.2f})")
print(f"Greatest Decrease in Profits: {lowProfMonth} ({lowProfit:.2f})")

#Write to File
outfile = open(os.path.join(pathlib.Path(__file__).parent.resolve(),'Analysis','PyBank_results.txt'),'x')
outfile.write("Financial Analysis\n")
outfile.write("  ---------------------------- \n")
outfile.write(f"Total Months: {len(months)}\n")
outfile.write(f"Total: {sumProfits:.2f}\n")
outfile.write(f"Average Change: {avgProfits:.2f}\n")
outfile.write(f"Greatest Increase in Profits: {highProfMonth} ({highProfit:.2f})\n")
outfile.write(f"Greatest Decrease in Profits: {lowProfMonth} ({lowProfit:.2f})\n")