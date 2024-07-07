import matplotlib.pyplot as plt
from collections import namedtuple

# Define the Rectangle namedtuple
Rectangle = namedtuple('Rectangle', 'bottomLeft topRight')

# Define the rectangles

rects = [Rectangle(bottomLeft=(53, 8), topRight=(120, 169)), Rectangle(bottomLeft=(25, 169), topRight=(193, 170)), Rectangle(bottomLeft=(10, 171), topRight=(99, 172)), Rectangle(bottomLeft=(144, 186), topRight=(175, 187)), Rectangle(bottomLeft=(33, 185), topRight=(152, 186)), Rectangle(bottomLeft=(121, 175), topRight=(178, 178)), Rectangle(bottomLeft=(10, 173), topRight=(66, 179)), Rectangle(bottomLeft=(94, 183), topRight=(100, 184)), Rectangle(bottomLeft=(70, 184), topRight=(143, 185)), Rectangle(bottomLeft=(48, 170), topRight=(92, 171)), Rectangle(bottomLeft=(167, 189), topRight=(194, 190)), Rectangle(bottomLeft=(109, 187), topRight=(194, 188)), Rectangle(bottomLeft=(90, 175), topRight=(102, 182)), Rectangle(bottomLeft=(174, 188), topRight=(181, 189)), Rectangle(bottomLeft=(124, 173), topRight=(148, 174)), Rectangle(bottomLeft=(32, 172), topRight=(175, 173)), Rectangle(bottomLeft=(5, 182), topRight=(187, 183)), Rectangle(bottomLeft=(164, 184), topRight=(186, 185)), Rectangle(bottomLeft=(43, 189), topRight=(155, 190))]

ax = plt.gca()
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
color_index = 0

for rect in rects:
    bottomLeft, topRight = rect.bottomLeft, rect.topRight
    width = topRight[0] - bottomLeft[0]
    height = topRight[1] - bottomLeft[1]
    
    # Use the next color in the cycle
    # color = color_cycle[color_index % len(color_cycle)]
    # color_index += 1
    # ax.add_patch(plt.Rectangle(bottomLeft, width, height, edgecolor=color, facecolor='none'))

    # Uncomment if you want to use same color each time
    ax.add_patch(plt.Rectangle(bottomLeft, width, height, edgecolor='teal', facecolor='none'))

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
