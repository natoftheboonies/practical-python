# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename,select=None,types=None,has_headers=True,delimiter=',',silence_errors=False):
	'''
	Parse a CSV file into a list of records
	'''
	with open(filename) as f:
		rows = csv.reader(f,delimiter=delimiter)
		
		if has_headers:
			headers = next(rows)		

		if select and not has_headers:
			raise RuntimeError("select argument requires column headers")

		if select:
			indices = [headers.index(col) for col in select]
			headers = select
		else:
			indices = None

		records = []
		for rowidx,row in enumerate(rows,start=1):
			if not row:
				continue

			if indices:
				row = [ row[index] for index in indices ]

			try:
				if types:
					row = [func(val) for func,val in zip(types,row)]
			except ValueError as e:
				if not silence_errors:
					print(f'Row {rowidx}: Couldn\'t convert {row}')
					print(f'Row {rowidx}: {e}')
				continue

			if has_headers:
				record = dict(zip(headers,row))
			else:
				record = row
			records.append(record)
	return records
