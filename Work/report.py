# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
	'Opens the filename and computes the portfolio cost'

	portfolio = []
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)

		for row in rows:
			try:
				holding = {'name':row[0],'shares':int(row[1]),'price':float(row[2])}
				portfolio.append(holding)
			except Exception as e:
				print('Failed',e,row)
		
	return portfolio

def read_prices(filename):
	'Opens the filename and reads as prices'

	prices = {}
	with open(filename) as f:
		rows = csv.reader(f)
		for row in rows:
			if len(row)>1:
				prices[row[0]]=float(row[1])

	return prices


prices = read_prices('Data/prices.csv')

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
portfolio = read_portfolio(filename)
#print(f'Total cost {cost:0.2f}')

total_gain = 0
total_value = 0

for holding in portfolio:
	cost = holding['shares']*holding['price']
	value = holding['shares']*prices.get(holding['name'],0)
	total_value += value
	total_gain += value-cost

print('value',total_value,'gain',total_gain)
