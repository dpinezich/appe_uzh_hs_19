import math

def volume_from_radius(radius):
    result = 4.0/3.0 * math.pi * radius**3
    return result

radius = int(input('Radius: '))

print(volume_from_radius(radius))