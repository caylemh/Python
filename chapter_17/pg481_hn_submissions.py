from operator import itemgetter
import requests
#from plotly.graph_objs import Bar
#from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

sub_dicts = submission_ids[]

print(sub_dicts)

"""
submission_dicts, titles, comments = [],[],[]

for submission_id in submission_ids[:30]:
	# Make a separate API call for each submission.
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	title = submission_dicts['title']
	comment = submission_dicts['comments']

	# Build a dictionary for each article.
	label = {
	'title': response_dict['title'],
	'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
	'comments': response_dict['descendants'],
	}
	submission_dicts.append(label)
	titles.append(title)
	comments.append(comment)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

# Make visualization.
data = [{
	'type': 'bar',
	'x': submission_dicts['title'],
	'y': submission_dicts['comments'],
	'hovertext': labels,
	'marker': {
		'color': submission_dicts['comment'],
		'colorscale': 'Portland',
		'line': {'width': 1.5, 'color':'rgb(25,25,25)'}
		},
	'opacity': 0.6,
}]
my_layout = {
	'title': 'Most Number of Comments per Article on Hackernews.com',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Article',
		'titlefont': {'size': 20},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Comments',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')

#for submission_dict in submission_dicts:
	#print(f"\nTitle: {submission_dict['title']}")
	#print(f"Discussion link: {submission_dict['hn_link']}")
	#print(f"Comments: {submission_dict['comments']}")
"""