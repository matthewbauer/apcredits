#!/usr/bin/python

import glob
import csv

import peewee

db = peewee.MySQLDatabase('apcredits', host="apcredits.ccpuvvzgbdch.us-west-2.rds.amazonaws.com", port=3306)

class Credit(peewee.Model):
	college = peewee.TextField()
	test = peewee.TextField()
	score = peewee.IntegerField()
	credit = peewee.IntegerField()
	_class = peewee.TextField()
	class Meta:
		database = db

db.connect()

colleges = {}

Credit.create_table()

with open("codes", 'r') as f:
	for line in f:
		v = line.split(' ')
		colleges[v[0]] = ' '.join(v[1:])

for filename in glob.glob('apinfo/*'):
	collegename = colleges[filename.split('/')[1]]
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		for row in reader:
#			print(row)
			if row is None or row is []:
				continue
			if len(row) == 4:
				if row[1] == '--':
					row[1] = -1
				if row[2] == '--':
					row[2] = -1
				Credit.create(college=collegename, test=row[0], score=row[1], credit=row[2], _class=row[3])
