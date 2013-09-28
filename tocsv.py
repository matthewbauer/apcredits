#!/usr/bin/python

from bs4 import BeautifulSoup
import glob
import csv

for filename in glob.glob('html/*'):
	print(filename)
	code = filename.split('/')[1]
	soup = BeautifulSoup(open(filename))
	writer = csv.writer(open('apinfo/%s' % code, 'w'), delimiter=';')
	oldvalues = ['', '', '', '']
	for row in soup.findAll('tr'):
		values = []
		for i, td in enumerate(row.findAll('td')):
			if td.string == None:
				values.append(oldvalues[i])
			else:
				values.append(td.string)
				oldvalues[i] = td.string
		writer.writerow(values)