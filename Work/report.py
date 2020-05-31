#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv

def read_portfolio(filename:str)->list:
	'Reads a portfolio from a CSV file including shares,prices data into a list of dictionaries'
	with open(filename) as f:
		portfolio = parse_csv(f,select=['name','shares','price'],types=[str,int,float])
	return portfolio

def read_prices(filename:str) -> dict:
	'Reads prices from a CSV file of name,price data'
	with open(filename) as file:
		pricelist = parse_csv(file,types=[str,float], has_headers=False)
		prices = dict(pricelist)
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


def portfolio_report(portfile:str,pricefile:str):
	portfolio = read_portfolio(portfile)
	prices = read_prices(pricefile)
	report = make_report(portfolio,prices)
	print_report(report)

def main(argv):
	portfile = 'Data/portfolio.csv'
	pricefile = 'Data/prices.csv'

	if len(argv) == 3:
		portfile = argv[1]
		pricefile = argv[2]

	portfolio_report(portfile,pricefile)	


if __name__=='__main__':
	import sys
	main(sys.argv)