from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D6 dice.

die_1, die_2 = Die(), Die()

#Make some rolls and multiply the two dice to get the result, and store results in a list
results =[]

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

#for roll_num in range(1000):
	#result = die_1.roll() + die_2.roll()
	#results.append(result)

#Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

frequencies = [results.count(value) for value in range(2,max_result+1)]

#for value in range(2,max_result+1):
	#freqency = results.count(value)
	#frequencies.append(freqency)

#Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='The results of rolling two D6 dice 1000 times.',
			xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='comp_d6_d6.html')