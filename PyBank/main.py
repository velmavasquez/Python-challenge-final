import os
import csv
budget_dataCSV = os.path.join('..', 'python-challenge', 'PyBank', 'budget_data.csv')

print("Financial Analyst")
print("---------------------------")
#The total number of months included in the dataset
with open(budget_dataCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    data = list(csvreader)
    months_count = len(data)
    print('Total Months: {}'.format(months_count))
#The net total amount of "Profit/Losses" over the entire period
with open(budget_dataCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    totalPL = 0
    for row in csv.reader(csvfile):
        totalPL += int(row[1])
    print(f"Total: $ {str(totalPL)}")

#The greatest decrease in losses (date and amount) over the entire period

with open(budget_dataCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    PLvalues = []
    PLchange = []
    date = []

    for row in csvreader:
        PLvalues.append(float(row[1]))
        date.append (row[0])

    for i in range (1,len(PLvalues)):

#The average of the changes in "Profit/Losses" over the entire period
        PLchange.append(PLvalues[i] - PLvalues[i-1])
        avgPLchange = sum(PLchange)/len(PLchange)

#The greatest increase in profits (date and amount) over the entire period
        greatest_in_profits = max(PLchange)     
        greatest_in_profits_date = str(date[PLchange.index(max(PLchange))])

#The greatest decrease in losses (date and amount) over the entire period
        greatest_de_profits = min(PLchange)
        greatest_de_profits_date = str(date[PLchange.index(min(PLchange))])
        
    print(f"Average Change: ${str(round(avgPLchange, 2))}")
    print(f"Greatest increase in Profits: {greatest_in_profits_date} (${str(round(greatest_in_profits))})")
    print(f"Greatest decrease in Profits: {greatest_de_profits_date} (${str(round(greatest_de_profits))})")

file = open("PyBank.txt","w")
file.write("Financial Analyst")
file.write("---------------------------")
file.write(f"Average Change: ${str(round(avgPLchange, 2))}")
file.write(f"Greatest increase in Profits: {greatest_in_profits_date} (${str(round(greatest_in_profits))})")
file.write(f"Greatest decrease in Profits: {greatest_de_profits_date} (${str(round(greatest_de_profits))})")
file.close()