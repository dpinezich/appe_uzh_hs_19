def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark/0.5)*0.5

marks = {}
max_points = input('Max Points: ')

while True:
    name = input('Name: ')
    if name == 'exit':
        break
    points = input('Points: ')
    marks[name] = calculate_mark(points, max_points)

print(marks)
print('Bye bye')