

import matplotlib.pyplot as plt


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
fig, ax = plt.subplots()
ax.plot(squares, linewidth = 3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()