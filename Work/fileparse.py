# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename,select=None,types=None,has_headers=True,delimiter=','):
	'''
	Parse a CSV file into a list of records
	'''
	with open(filename) as f:
		rows = csv.reader(f,delimiter=delimiter)
		
		if has_headers:
			headers = next(rows)

		if select:
			indices = [headers.index(col) for col in select]
			headers = select
		else:
			indices = None

		records = []
		for row in rows:
			if not row:
				continue
			if indices:
				row = [ row[index] for index in indices ]

			if types:
				row = [func(val) for func,val in zip(types,row)]

			if has_headers:
				record = dict(zip(headers,row))
			else:
				record = row
			records.append(record)
	return records
