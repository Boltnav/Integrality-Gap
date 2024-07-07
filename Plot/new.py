import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the rectangles with bottom-left and top-right coordinates
rectangles = [
    {'label': '0', 'bottomLeft': (24, 4), 'topRight': (39, 90)},
    {'label': '1', 'bottomLeft': (35, 13), 'topRight': (51, 91)},
    {'label': '2', 'bottomLeft': (19, 12), 'topRight': (23, 78)},
    {'label': '3', 'bottomLeft': (64, 48), 'topRight': (82, 51)},
    {'label': '4', 'bottomLeft': (35, 40), 'topRight': (55, 64)},
    {'label': '5', 'bottomLeft': (6, 73), 'topRight': (87, 92)},
    {'label': '6', 'bottomLeft': (89, 45), 'topRight': (99, 53)},
    {'label': '7', 'bottomLeft': (29, 52), 'topRight': (79, 92)},
    {'label': '8', 'bottomLeft': (52, 16), 'topRight': (100, 25)},
    {'label': '9', 'bottomLeft': (14, 8), 'topRight': (52, 9)}
]

# Create a plot
fig, ax = plt.subplots()

# Add each rectangle to the plot
for rect in rectangles:
    bottom_left = rect['bottomLeft']
    width = rect['topRight'][0] - bottom_left[0]
    height = rect['topRight'][1] - bottom_left[1]
    rect_patch = patches.Rectangle(bottom_left, width, height, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect_patch)
    # Add label
    label_x = bottom_left[0] + width / 2
    label_y = bottom_left[1] + height / 2
    ax.text(label_x, label_y, rect['label'], horizontalalignment='center', verticalalignment='center')

# Set limits and show grid
ax.set_xlim(0, 110)
ax.set_ylim(0, 100)
ax.grid(True)

# Show the plot
plt.show()
