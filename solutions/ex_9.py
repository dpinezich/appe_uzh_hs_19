def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark/0.5)*0.5

while True:
    points = input('Points: ')
    if points == 'exit':
        print('Bye bye')
        break
    max_points = input('Max Points: ')
    print('Your Mark: ' + str(calculate_mark(points, max_points)))