
dict = {'name': 'David', 'age': 32}

for (my_key, my_value) in dict.items():
    if(my_key == 'age'):
        print('Not telling you this')
    else:
        print(my_key + ' : ' + my_value)
