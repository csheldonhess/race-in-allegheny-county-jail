import csv

# data aggregation variables
total_inmates = 0
total_black_inmates = 0
total_white_inmates = 0
total_asian_inmates = 0
total_hispanic_inmates = 0
total_indigenous_inmates = 0
total_unknown_race_inmates = 0

with open('jail_census_07_2017.csv', 'r') as census:
	censusreader = csv.DictReader(census)
	for row in censusreader:
		if row['Date'] == '2017-07-01':
			if row['Race'] == 'B':
				total_black_inmates += 1
			elif row['Race'] == 'W':
				total_white_inmates += 1
			elif row['Race'] == 'A':
				total_asian_inmates += 1
			elif row['Race'] == 'H':
				total_hispanic_inmates += 1
			elif row['Race'] == 'I':
				total_indigenous_inmates += 1
			else:
				total_unknown_race_inmates += 1
			total_inmates += 1


with open('README.md', 'a') as output:
	output.write('\n\t* Total inmates: %i\n' %total_inmates)
	output.write('\t* Total Black inmates: %i, %.2f%%\n' %(total_black_inmates, total_black_inmates/total_inmates * 100))
	output.write('\t* Total Asian inmates: %i, %.2f%%\n' %(total_asian_inmates, total_asian_inmates/total_inmates * 100))
	output.write('\t* Total Hispanic inmates: %i, %.2f%%\n' %(total_hispanic_inmates, total_hispanic_inmates/total_inmates * 100))
	output.write('\t* Total Indigenous inmates: %i, %.2f%%\n' %(total_indigenous_inmates, total_indigenous_inmates/total_inmates * 100))
	output.write('\t* Total white inmates: %i, %.2f%%\n' %(total_white_inmates, total_white_inmates/total_inmates * 100))
	output.write('\t* Total inmates of unknown race: %i, %.2f%%\n' %(total_unknown_race_inmates, total_unknown_race_inmates/total_inmates * 100))

