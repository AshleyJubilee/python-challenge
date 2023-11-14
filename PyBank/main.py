import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

monthTotal = 0
profitTotal  = 0
profitChange = 0
changeList  = []
firstMonth = 0
lastMonth = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    #Stores and skips header
    csvHeader = next(csvreader)

    # Counts number of rows after header, number of months
    for row in csvreader:
        monthTotal += 1
        profitTotal += int(row[1])

        if firstMonth == 0:
            firstMonth = int(row[1])
            continue
        else: 
            lastMonth = int(row[1])

    totalChange = lastMonth - firstMonth
    averageChange = totalChange / monthTotal


    print(f"Total Months: {monthTotal}")
    print(f"Total Profit: ${profitTotal}")
    print(f"Average Change: ${averageChange}")
          



    

        

