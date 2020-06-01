#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import csv
import sys
import report

def portfolio_cost(filename):
	'Opens the filename and computes the portfolio cost'
	portfolio = report.read_portfolio(filename)
	total_cost = 0
	for s in portfolio:
		total_cost += s.cost	
	return total_cost


def main(argv):
	portfile = 'Data/portfolio.csv'

	if len(argv) == 2:
		portfile = argv[1]

	cost = portfolio_cost(portfile)
	print(f'Total cost {cost:0.2f}')	


if __name__=='__main__':
	import sys
	main(sys.argv)

