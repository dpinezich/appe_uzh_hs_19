import math

#from ex2
def volume_from_radius(radius):
    return 4.0/3 * math.pi * radius**3

# from ex3
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def volume_from_points(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y1)
    return volume_from_radius(radius)

x1 = int(input('Point 1 x-cord: '))
y1 = int(input('Point 1 y-cord: '))
x2 = int(input('Point 2 x-cord: '))
y2 = int(input('Point 2 y-cord: '))

print(volume_from_points(x1, y1, x2, y2))