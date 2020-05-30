# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
	'Opens the filename and loads the portfolio as a dictionary'

	portfolio = []
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)
		for num, row in enumerate(rows,start=1):
			record = dict(zip(headers,row))
			try:
				record['shares'] = int(record['shares'])
				record['price'] = float(record['price'])
				portfolio.append(record)
			except ValueError:
				print(f'Row {num}: Couldn\'t convert {row}')
				
	return portfolio

def read_prices(filename):
	'Opens the filename and reads as prices as a dictionary'

	prices = {}
	with open(filename) as f:
		rows = csv.reader(f)
		for row in rows:
			if len(row)>1:
				prices[row[0]]=float(row[1])

	return prices

def make_report(portfolio, prices):
	rows = []
	for holding in portfolio:
		current_price = prices[holding['name']]
		row = (holding['name'],holding['shares'],prices[holding['name']],holding['price']-current_price)
		rows.append(row)
	return rows


prices = read_prices('Data/prices.csv')

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
portfolio = read_portfolio(filename)
#print(f'Total cost {cost:0.2f}')

report = make_report(portfolio,prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' %headers)
print((' '+'-'*10)*4)

for name,shares,price,change in report:
	fprice = '$'+f'{price:0.2f}'
	print(f'{name:>10s} {shares:>10d} {fprice:>10s} {change:>10.2f}')
