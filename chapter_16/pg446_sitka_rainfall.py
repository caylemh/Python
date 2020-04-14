import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

#print(header_row)

	# Get the dates and high temperatures from this file.
	prcps, dates = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			prcp = float(row[3])
		except ValueError:
			print(f'Missing data for {current_date}')
		else:
			dates.append(current_date)
			prcps.append(prcp)

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue', alpha=0.5)

#Format plot.
title = 'Precipitation Values - 2018\nSitka Rainfall Data'
plt.title(title, fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()