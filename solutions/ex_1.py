def compare(x, y):
    if x > y:
        print(1)
    elif x == y:
        print(0)
    else:
        print(-1)


x = int(input('first number '))
y = int(input('second number '))

compare(x, y)