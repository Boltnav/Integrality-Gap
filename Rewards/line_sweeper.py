from collections import namedtuple

# Rectangle = namedtuple('Rectangle', field_names= ['bottomLeft', 'topRight'])
Rectangle = namedtuple('Rectangle', 'id bottomLeft topRight')

def intervalsIntersect(int1, int2):
    return not (int1[0] >= int2[1] or int2[0] >= int1[1])

def isIntersecting(rect1, rect2):
    xInterval1 = (rect1.bottomLeft[0], rect1.topRight[0])
    xInterval2 = (rect2.bottomLeft[0], rect2.topRight[0])
    yInterval1 = (rect1.bottomLeft[1], rect1.topRight[1])
    yInterval2 = (rect2.bottomLeft[1], rect2.topRight[1])
    return intervalsIntersect(xInterval1, xInterval2) and intervalsIntersect(yInterval1, yInterval2)

def line_sweeper(rects):
    events = []
    active_rects = []
    constraints = []
    for idx, rect in enumerate(rects):
        events.append((rect.bottomLeft[0], 'start', idx))
        events.append((rect.topRight[0], 'end', idx))
    events.sort(key=lambda x: (x[0], x[1] == 'end'))

    for event in events:
        x, typ, idx = event
        rect = rects[idx]
        if typ == 'start':  # check for intersections with active rectangles
            for active_idx in active_rects:
                active_rect = rects[active_idx]
                if isIntersecting(rect, active_rect):   # intersection found, record constraint
                    constraints.append(sorted([idx, active_idx]))
            # add current rectangle to active rectangles
            active_rects.append(idx)
        elif typ == 'end':
            # remove from active rectangles
            active_rects.remove(idx)

    return constraints

# Example rectangles
# rects = [
#     Rectangle(id=0, bottomLeft=(52, 4), topRight=(69, 71)),
#     Rectangle(id=1, bottomLeft=(41, 72), topRight=(60, 91)),
#     # Add other rectangles as needed
# ]
rects = [
    Rectangle(id=0, bottomLeft=(52, 4), topRight=(69, 71)),
    Rectangle(id=1, bottomLeft=(41, 72), topRight=(60, 91)),
    Rectangle(id=2, bottomLeft=(60, 32), topRight=(87, 97)),
    Rectangle(id=3, bottomLeft=(11, 19), topRight=(84, 36)),
    Rectangle(id=4, bottomLeft=(3, 74), topRight=(12, 85)),
    Rectangle(id=5, bottomLeft=(60, 32), topRight=(96, 63)),
    Rectangle(id=6, bottomLeft=(29, 6), topRight=(63, 100)),
    Rectangle(id=7, bottomLeft=(46, 54), topRight=(86, 75)),
    Rectangle(id=8, bottomLeft=(12, 93), topRight=(60, 96)),
    Rectangle(id=9, bottomLeft=(32, 22), topRight=(100, 88)),
    Rectangle(id=10, bottomLeft=(43, 19), topRight=(93, 64)),
    Rectangle(id=11, bottomLeft=(21, 5), topRight=(62, 61)),
    Rectangle(id=12, bottomLeft=(60, 14), topRight=(95, 65)),
    Rectangle(id=13, bottomLeft=(26, 20), topRight=(48, 34)),
    Rectangle(id=14, bottomLeft=(12, 35), topRight=(91, 87)),
    Rectangle(id=15, bottomLeft=(68, 39), topRight=(69, 44)),
    Rectangle(id=16, bottomLeft=(17, 20), topRight=(53, 49)),
    Rectangle(id=17, bottomLeft=(95, 61), topRight=(99, 84)),
    Rectangle(id=18, bottomLeft=(26, 56), topRight=(28, 57))
]


constraints = line_sweeper(rects)
print("Constraints between rectangles:", constraints)
