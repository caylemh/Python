import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.plot(input_values, y_values, linewidth=3)
ax.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Oranges, s=10)

#Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)

#Set the range foe each axis.
ax.axis([0,1100,0,1100000])
ax.ticklabel_format(axis='y', style='plain')

plt.show()
#plt.savefig('squares_plt.png', bbox_inches='tight')