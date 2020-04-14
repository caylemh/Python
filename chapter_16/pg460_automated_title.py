import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/1.0_month.geojson'
with open(filename) as f:
	all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
eq_title = all_eq_data['metadata']

mags, lons, lats, hover_texts = [],[],[],[]
for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])
	hover_texts.append(eq_dict['properties']['title'])

#Map the earthquakes
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Hot',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
		},
	}]

my_layout = Layout(title=eq_title['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
#print(mags[:10])
#print(lons[:5])
#print(lats[:5])