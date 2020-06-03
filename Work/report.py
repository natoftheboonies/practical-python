#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import sys
import stock
from fileparse import parse_csv
import tableformat
from portfolio import Portfolio

def read_portfolio(filename:str)->list:
	'Reads a portfolio from a CSV file including shares,prices data into a list of Stock instances'
	with open(filename) as f:
		portdicts = parse_csv(f,select=['name','shares','price'],types=[str,int,float])
	portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]		
	return Portfolio(portfolio)

def read_prices(filename:str) -> dict:
	'Reads prices from a CSV file of name,price data'
	with open(filename) as file:
		pricelist = parse_csv(file,types=[str,float], has_headers=False)
		prices = dict(pricelist)
	return prices

def make_report(portfolio:list, prices:dict)->list:
	rows = []
	for holding in portfolio:
		current_price = prices[holding.name]
		row = (holding.name,holding.shares,prices[holding.name],holding.price-current_price)
		rows.append(row)
	return rows

def print_report(report:list,formatter)->None:
	headers = ['Name', 'Shares', 'Price', 'Change']
	formatter.headings(headers)
	#print('%10s %10s %10s %10s' %headers)
	#print((' '+'-'*10)*4)

	for name,shares,price,change in report:
		fprice = '$'+f'{price:0.2f}'
		rowdata = [ name, str(shares), fprice, f'{change:0.2f}' ]
		formatter.row(rowdata)
		#print(f'{name:>10s} {shares:>10d} {fprice:>10s} {change:>10.2f}')


def portfolio_report(portfile:str,pricefile:str,fmt='txt'):
	portfolio = read_portfolio(portfile)
	prices = read_prices(pricefile)
	report = make_report(portfolio,prices)

	formatter = tableformat.create_formatter(fmt)
	print_report(report,formatter)

def main(argv):
	portfile = 'Data/portfolio.csv'
	pricefile = 'Data/prices.csv'
	fmt = 'txt'

	if len(argv) > 1:
		portfile = argv[1]
		pricefile = argv[2]
		fmt = argv[3]

	portfolio_report(portfile,pricefile,fmt)	


if __name__=='__main__':
	import sys
	main(sys.argv)