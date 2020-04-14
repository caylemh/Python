import csv

import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'data/death_valley_2018_simple.csv'


def get_data(filename, dates, prcps):

	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		print(header_row)

		date_index = header_row.index('DATE')
		prcp_index = header_row.index('PRCP')
		name_index = header_row.index('NAME')

		global place_name
		place_name =""

		for row in reader:
			# Grab the station name, if it's not already set.
			if not place_name:
				place_name = row[name_index]
				print(place_name)

			current_date = datetime.strptime(row[date_index], '%Y-%m-%d')

			#Check if there are values present
			try:
				prcp = float(row[prcp_index])
			except ValueError:
				print(f'Missing values for: {current_date}')
			else:
				dates.append(current_date)
				prcps.append(prcp)

#Get Sitka data
filename = 'data/sitka_weather_2018_simple.csv'
dates, prcps = [],[]
	
#Get Death Valley data
filename1 = 'data/death_valley_2018_simple.csv'
dates1, prcps1 = [],[]

#Get Death Valley data
filename2 = 'data/san_francisco_2018_summary.csv'
dates2, prcps2 = [],[]

#Plot the high and low temperatures.
plt.style.use('seaborn')
#fig, (ax, ax1) = plt.subplots(2,1, num='Precipitation Values 2018')

plt.subplots_adjust(hspace=1)

#Plot Sitka's values
get_data(filename,dates,prcps)
plt.subplot(3,1,1)
plt.plot(dates, prcps, c='red', alpha=0.5)
plt.title('SITKA AIRPORT, AK US')
plt.ylabel('Precipitation', fontsize=12)


#Plot Death valley's values
get_data(filename1,dates1,prcps1)	
plt.subplot(3,1,2)
plt.plot(dates1, prcps1, c='blue', alpha=0.5)
plt.title('DEATH VALLEY, CA US', pad=3)
plt.ylabel('Precipitation', fontsize=12)

#Plot Death valley's values
get_data(filename2,dates2,prcps2)	
plt.subplot(3,1,3)
plt.plot(dates2, prcps2, c='orange', alpha=0.5)
plt.title('OAKLAND 4.9 NNE, CA US', pad=3)
plt.ylabel('Precipitation', fontsize=12)

plt.show()