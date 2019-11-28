import json

address_book_file = open('address_book.txt', 'r')

address_book_dict = json.load(address_book_file)
    
while True:
    requested_name = input('Name zur Suche eingeben: ')
    if requested_name == 'exit':
        break
    else:
        if requested_name in address_book_dict:
            print(address_book_dict[requested_name])
        else:
            print('Person nicht gefunden')

address_book_file.close()