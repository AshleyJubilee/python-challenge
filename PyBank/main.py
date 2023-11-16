import os
import csv
import statistics

csvpath = os.path.join("Resources", "budget_data.csv")
outputpath = os.path.join("analysis", "analysis.txt")

monthTotal = 0
profitTotal  = 0
profitChange = 0
changeList = []
currentMonth = 0
lastMonth = 0
averageChange = 0
greatestInc = 0
greatestIncMonth = ''
greatestDec = 0
greatestDecMonth = ''
diff = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    # Stores and skips header
    csvHeader = next(csvreader)

    # Loops through each row and updates vairables
    for row in csvreader:

        # Counts total monthts and total profits
        monthTotal += 1
        profitTotal += int(row[1])

        currentMonth = int(row[1])
      
        # Skips first month since there is no 'last month' to compare the current value to
        if lastMonth == 0: 
            lastMonth = int(row[1])
            continue
        else:

            # Updates current difference and adds it to the list
            diff = -(lastMonth - currentMonth)

            changeList.append(diff)

            # Finds the mean of all month to month differences
            averageChange = round(statistics.mean(changeList),2)

            # Updates greatest change variables
            if diff > greatestInc:
                greatestInc = diff
                greatestIncMonth = row[0]
        
            if diff < greatestDec:
                greatestDec = diff
                greatestDecMonth = row[0]

            # Sets the lastMonth value for the next loop
            lastMonth = int(row[1])

    analysis = [f"Total Months: {monthTotal}",
        f"Total Profit: ${profitTotal}", 
        f"Average Change: ${averageChange}", 
        f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})", 
        f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})"]
    
    # Adds line breaks
    joinAnalysis = '\n'.join(analysis)

    print(joinAnalysis)

# Export to new file
with open(outputpath, "w") as f:
    f.write(joinAnalysis)
          



    

        

