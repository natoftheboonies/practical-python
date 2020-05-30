# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
	'Opens the filename and computes the portfolio cost'
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)

		total_cost = 0
		for row in rows:
			try:
				total_cost += int(row[1])*float(row[2])
			except Exception as e:
				print('Failed',e,row)
		
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost {cost:0.2f}')