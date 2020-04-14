import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/JHB_2070744.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get the dates and high temperatures from this file.
	prcps, dates = [], []
	for row in reader:
		current_date = datetime.strptime(row[5], '%Y-%m-%d')
		try:
			prcp = float(row[8])
		except ValueError:
			print(f'Missing data for {current_date}')
		else:
			dates.append(current_date)
			prcps.append(prcp)

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='red', alpha=0.5)

#Format plot.
title = 'Precipitation Values - 1915 to 1996\nJHB Zoological Gardens, RSA'
plt.title(title, fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation (mm)',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()