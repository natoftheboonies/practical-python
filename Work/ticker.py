# ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
	for row in rows:
		yield [row[index] for index in indices]


def convert_types(rows, types):
	for row in rows:
		yield [func(val) for func, val in zip(types, row)]


def parse_stock_data(lines):
	rows = csv.reader(lines)
	rows = select_columns(rows, [0,1,4])
	rows = convert_types(rows, [str,float,float])
	rows = (dict(zip(['name','price','change'],row)) for row in rows)
	return rows

def ticker(portfile,logfile,fmt):
	import report
	portfolio = report.read_portfolio(portfile)
	lines = follow(logfile)
	rows = parse_stock_data(lines)
	rows = (row for row in rows if row['name'] in portfolio)
	#rows = filter_symbols(rows, portfolio)
	import tableformat
	formatter = tableformat.create_formatter(fmt)
	formatter.headings(['Name','Price','Change'])
	for row in rows:
		rowdata = [row['name'],str(row['price']),str(row['change'])]
		formatter.row(rowdata)


if __name__=='__main__':
	ticker('Data/portfolio.csv','Data/stocklog.csv','txt')	
