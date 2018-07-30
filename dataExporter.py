import csv
import pandas

cols = ['State', 'NO2_AVG_2000', 'NO2_AVG_2001', 'NO2_AVG_2002', 'NO2_AVG_2003', 
'NO2_AVG_2004', 'NO2_AVG_2005', 'NO2_AVG_2006', 'NO2_AVG_2007', 'NO2_AVG_2008',
'NO2_AVG_2009', 'NO2_AVG_2010', 'NO2_AVG_2011', 'NO2_AVG_2012', 'NO2_AVG_2013',
'NO2_AVG_2014', 'NO2_AVG_2015', 'NO2_AVG_2016']

states = []
lst = []

with open('NO2_Pollutant.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t', quotechar='|')

	for row in reader:
		print(row[2])


for row in lst:
	print(row[0])





