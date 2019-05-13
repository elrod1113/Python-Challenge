import csv
import os

months = [] 
revenue = []


total_months = 0
net_total = 0
average = 0
greatest_increase = 0
greatest_dearease = 0

with open(file_analyze, newline-"") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    storage = {} # csv file data
    monthchange = [] #change_in_revenue
    final = # dictionary for data storage
    answer = [] # for answers

    for row in csvreader: # Dictionary
        if row[0] != 'Date': # exclude first row
            storage[row[0]] = int(row[1])

totalmonth = len(storage) # Number of month = number of keys
totalrevenue = sum(storage.values()) # total revenue for period
revs = tuple(storage.values())
month = tuple(storage.keys())

for x in range(1, (len(revs))): #revenue changes
    monthchange.append(int(revs[x]) - int(revs[x-1]))
average = round(mean(monthchange)) #Change in revenue

maxincrease = max(zip(final.values(), final.keys()))
mindecrease = min(zip(final.values(), final.keys()))

answer.append('Financial Analysis')
answer.append('Total months: ' + str(totalmonth))
answer.append('Total Revenue: $' + str(totalrevenue))
answer.append(Average Revenue Change: $' + str(average))
answer.append(Greatest increase in revenue: ' + str(minincrease[1] +'($' +(maxincrease')[0]) + ')
answer.append(Greatest decrease in revenue: ' + str(mindecrease[1] +'($' +(maxdecrease')[0]) + ')
print("\n".join((answer)))

with open(newfile, 'w') as txtfile:
    txtfile.write('\n'.join(answer))