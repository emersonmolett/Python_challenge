import os
import csv

csvpath = os.path.join('Resources','02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
months =[]
profit_losses =[]

average_revenue = int()

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    header_row = next(csvreader)


    #read each row of data
    for row in csvreader:

        #add months
        months.append(row[0])

        #add profit
        profit_losses.append(int(row[1]))



print('Financial Analysis:')
#calculate total months
total_months = len(months)
print ('Total months:')
print(total_months)

print('Net Total:')
#calculate net total amount of profit losses
net_total = sum(profit_losses)
print(net_total)

#average change
average_change = net_total/total_months
print('This is the average profit/losses: ' + str(average_change))

greatest_increase = ['',0]
greatest_decrease = ['', 99999999999999999999999999999999999999]
revenue_change = []
