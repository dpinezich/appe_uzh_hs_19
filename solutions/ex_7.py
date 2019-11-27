def print_reverse(text):
    counter = len(text)-1
    str = ''

    while counter >= 0:
        str = str + text[counter]
        counter = counter - 1
    print(str)

string = input('String: ')
print_reverse(string)
