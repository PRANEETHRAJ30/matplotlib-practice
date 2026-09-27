#import
from matplotlib import pyplot as plt
plt.style.use('ggplot') #used for styles
#import the data
#Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#Median Salaries
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


# Median Python Developer Salaries by Age
#we have same x values so we using only one time and ploting
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

#plot1
plt.plot(ages_x, dev_y)
#plot 2
plt.plot(ages_x, py_dev_y)

#label x and y label
plt.xlabel('Ages')
plt.ylabel('Salary')

#give title to plot
plt.title('Median Salary by Age')

#legends- suppose we have more than two lines in graph we dont which line represents what so we use legends
#plot 1 legend
plt.legend(['All_Devs', 'Python'])

# we can plot label in otehr way
#plot1
plt.bar(ages_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs', linewidth=3) #format strings are used ti change the line colors, amrkers etc here k and b are format string (k--dotted)(b-blue line)
#plot 2
plt.bar(ages_x, py_dev_y, 'b', marker='o', label='Python',linewidth=3)

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(ages_x, js_dev_y, color='#adad3b',label='Javascript',linewidth=3)

#label x and y label
plt.xlabel('Ages')
plt.ylabel('Salary')

#give title to plot
plt.title('Median Salary by Age')
plt.legend()

#Grid
# plt.grid(True)

#Padding
plt.tight_layout()

#to save plot graph
plt.savefig('plot.png')


#**************BAR GRAPH*****************
# plt.bar(ages_x, dev_y, color="#444444", label="All Devs")
plt.show() #to show output


