#Setting up csv import
import os
import csv
#Getting file path (Note: Must be run from main Python-Challenge folder, otherwise it will not find the file)
csvpath =  os.path.join("PyBank", "Resources", "budget_data.csv")
#Iterating on csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skipping the first row
    next(csvreader)
    #Defining variables for later use in for loops
    maximum = 0
    minimum = 0
    profit = []
    months = []
    change = []
    #Separating data into lists
    for row in csvreader:
        profit.append(int(row[1]))
        months.append(row[0])
    #Setting baseline for profit change loop
    initial_profit = int(profit[0])
    #Profit change loop
    for x in range(1, len(profit)):
        change.append(int(profit[x])-initial_profit)
        initial_profit = int(profit[x])
    #First three calculations (Total profit, total months, average profit change)
    total = sum(profit)
    total_months = len(months)
    avg_change = sum(change)/len(change)
    #Removing the first month to match up with the change list
    #There is no change from Jan-10, so to index properly, this seemed simplest. Setting month index to x + 1 could also work, however
    months.remove(months[0])
    #Finding the minimum and maximum change, and the index of its occurrence
    for x in range(0,len(change)):
        if change[x]>maximum:
            maximum = change[x]
            max_index = x
        if change[x]<minimum:
            minimum = change[x]
            min_index = x
#Storing results as text list
text = ["Financial Analysis",
    ("--------------------------"),
    ("Total Months: " + str(total_months)),
    ("Total: $" + str(total)),
    ("Average Change: $"+str(round(avg_change,2))),
    ("Greatest Increase in Profits: " + months[max_index] + " ($" + str(maximum) + ")"),
    ("Greatest Decrease in Profits: " + months[min_index] + " ($" + str(minimum) + ")")]
#Printing results
for x in range(len(text)):
    print(text[x])
#Getting file path
analysis_path = os.path.join("PyBank", "Analysis", "Analysis.txt")
#Writing text file
with open(analysis_path, 'w') as txt:
    #Leaving the last element out of the for loop avoids an extra page break
    for x in range(0, (len(text)-1)):
        txt.write(text[x] + '\n')
    #The last element is written here instead
    txt.write(text[len(text)-1])