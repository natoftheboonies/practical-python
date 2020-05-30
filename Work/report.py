# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename:str)->list:
	'Reads a portfolio from a CSV file including shares,prices data into a list of dictionaries'

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

def read_prices(filename:str) -> dict:
	'Reads prices from a CSV file of name,price data'

	prices = {}
	with open(filename) as f:
		rows = csv.reader(f)
		for row in rows:
			if len(row)>1:
				prices[row[0]]=float(row[1])

	return prices

def make_report(portfolio:list, prices:dict)->list:
	rows = []
	for holding in portfolio:
		current_price = prices[holding['name']]
		row = (holding['name'],holding['shares'],prices[holding['name']],holding['price']-current_price)
		rows.append(row)
	return rows

def print_report(report:list)->None:
	headers = ('Name', 'Shares', 'Price', 'Change')
	print('%10s %10s %10s %10s' %headers)
	print((' '+'-'*10)*4)

	for name,shares,price,change in report:
		fprice = '$'+f'{price:0.2f}'
		print(f'{name:>10s} {shares:>10d} {fprice:>10s} {change:>10.2f}')


def portfolio_report(portfolio_file:str,prices_file:str):
	portfolio = read_portfolio(portfolio_file)
	prices = read_prices(prices_file)
	report = make_report(portfolio,prices)
	print_report(report)


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

portfolio_report(filename,'Data/prices.csv')	
