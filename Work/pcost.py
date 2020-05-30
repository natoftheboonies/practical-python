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
		for num, row in enumerate(rows,start=1):
			record = dict(zip(headers,row))
			try:
				nshares = int(record['shares'])
				price = float(record['price'])
				total_cost += nshares * price
			except ValueError:
				print(f'Row {num}: Couldn\'t convert {row}')
		
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost {cost:0.2f}')