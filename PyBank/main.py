# Create script that can:
# Total the number of months, included in the dataset
# Net the total of months of 'Profit/Losses' over the entire dataset period
# Determine the greatest increase in profit over the entire period - this should include the date & amount
# Determine the greatest decrease in profit over the entire period - this should include the date & amount

import os
import csv

# Variables

months = []
profit_loss_changes = []
mount_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
count_months = 0 

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    header_row = next(csvreader)

    for row in csvreader:
        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# Export Text

with open("02-Homework_03-Python_Instructions_PyBank_Resources_budget_data", "w") as txt_file:
    txt_file.write('Financial Analysi' )
    txt_file.write('------------------- ')
    txt_file.write(f'Total Months: {count_months} ')
    txt_file.write(f'Total: ${net_profit_loss} ')
    txt_file.write(f'Average Change: ${average_profit_loss} ')
    txt_file.write(f'Greates Increase in Profits: {best_month} (${highest_change}) ')
    txt_file.write(f'Greatest Decease in Losses: {worst_month} (${lowest_change}) ')