# We need to import the OS module

import os

# Module for reading CSV files
import csv

csv = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

print(csvreader)

csv_reader = next(csvreader)
print(f'CSV Header: {csv_header}')

for row in csvreader:
	print(row)
	