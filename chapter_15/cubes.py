import matplotlib.pyplot as plt

#Plotting the first 5000 cubic numbers
plt.style.use('seaborn')
fig, ax = plt.subplots()

x_values = range(0,5001)
y_values = [x**2 for x in x_values]

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Oranges, s=10) # Adding a colormap: Orange

#Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)

#Set the range for each axis.
ax.axis([0,5100,0,25100000])

plt.show()