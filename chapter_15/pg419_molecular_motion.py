import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walks, as long as the program is active
while True:
	#Make a random walk.
	rw = RandomWalk(5_000)
	rw.fill_walk()

	#Plot the points in the walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,8))

	#point_numbers = range(rw.num_points)

	#Plotting a grain of pollen on a surface of water .
	ax.plot(rw.x_values, rw.y_values, linewidth=2, alpha=0.5)

	# Emphasize the first and last points.
	ax.scatter(0, 0, c='green', edgecolors='none', s=120)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
	s=120)

	# Remove the axes.
	#ax.get_xaxis().set_visible(False)
	#ax.get_yaxis().set_visible(False)

	#Show the plot
	plt.show()

	keep_running = input('Make another walk? (y/n): ')
	if keep_running == 'n':
		break