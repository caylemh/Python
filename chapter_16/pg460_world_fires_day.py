import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get the LONGITUDE, LATITUDE AND BRIGHTNESS of the fires from this file.
	lons, lats, brights, dates = [],[],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[5], '%Y-%m-%d')
		except IndexError:
			print(f'Missing index at {current_date}')

		lon = float(row[1])
		lat = float(row[0])
		bright = round(float(row[2]),2)
		dates.append(current_date)
		lons.append(lon)
		lats.append(lat)
		brights.append(bright)

#Map the earthquakes
data = [{
	'type': 'scattergeo',
	'lon': lons[:10000],
	'lat': lats[:10000],
	'marker': {
		'size': [bright/25 for bright in brights[:10000]],
		'color': brights,
		'colorscale': 'Cividis',
		'reversescale': True,
		'colorbar': {'title': 'Fire Brightness'}
		},
	}]

my_layout = Layout(title='World Fires: 24 Hour Results')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_day.html')
#print(mags[:10])
#print(lons[:5])
#print(lats[:5])