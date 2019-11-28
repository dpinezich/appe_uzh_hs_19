

file = open('my_text.txt', 'r')

i = 0
for line in file:
    if i % 2 == 0:
        line = line.strip()
        print(line)
    i = i+1

file.close()