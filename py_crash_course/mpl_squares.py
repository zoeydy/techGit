

from shutil import which
import fontTools
import matplotlib.pyplot as plt

########
# plot #
########
squares = []
i = 1
while i < 6:
    squares.append(i**2)
    i += 1
squares

fig, ax = plt.subplots() # subplots() generate one or more plots in the same figure
ax.plot(squares)
plt.show()

############################################
# change the label type and line thickness #
############################################
# 1
fig, ax = plt.subplots()
ax.plot(squares, linewidth = 3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()

# 2
# notice that the x axix value and y axis value are not plotted accordingly (starts at 0)
# let's fix that: give input and output value specifically
inpu = [1,2,3,4,5]
oupu = squares

fig, ax = plt.subplots()
ax.plot(inpu, oupu, linewidth = 3)
plt.show()

#########################
# Using built-in styles #
#########################
plt.style.available

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(inpu, oupu, linewidth = 3)
plt.show()

##########################################################
#  Plotting and styling individual points with scatter() #
##########################################################
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2,4)

plt.show()

fig, ax = plt.subplots()
# styling
ax.scatter(2,4,s=200)

# set chat title and label axes
ax.set_title("square numbers", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("square of value", fontsize = 14)

# set size of tick labels
ax.tick_params(axis='both', which = 'major', labelsize = 14)

plt.show()

###############################################
#  Plotting a series of Points with scatter() #
###############################################
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

ax.set_title("square numbers", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("square of value", fontsize = 14)

ax.tick_params(axis='both', which = 'major', labelsize = 14)

plt.show()

##################################
# Calculating Data Automatically #
##################################
