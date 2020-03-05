import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

# subplots can generate many plots in the same figure. Var fig represents the whole collection of plots
# variable x represents one single plot
plt.style.use('seaborn')
# you can use lots of styles built in
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set char title and axes
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both", labelsize=14)

plt.show()