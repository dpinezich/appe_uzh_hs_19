

def calc_sum(numbers):
    counter = 0
    total = 0

    while counter < len(numbers):
        total = total + numbers[counter]
        print('counter: ' + str(counter) + ' total ' + str(total))
        counter = counter + 1
    return total

print(calc_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

