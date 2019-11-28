# You first have to run in your console (if it is not automatically installed)
# pip install requests
# pip install bs4
# pip install pandas

from bs4 import BeautifulSoup
import pandas
import requests
import re

def extract_books_from_result(soup):
    returner = {'books': [], 'authors': []}
    for book in soup.find_all('div', attrs={'class':'cmp-text text'}):

        text = book.text
        pattern = re.compile(r'(?<=.).+(?=\n)')
        appender = re.findall(pattern, text)[0].split('by')

        # Including a condition just to avoid anything that’s not a book
        # Each book should consist in a list with two elements:
        # [0] = title and [1] = author

        if len(appender) > 1:
            returner['books'].append(appender[0])
            returner['authors'].append(appender[1])

    returner_df = pandas.DataFrame(returner, columns=['books', 'authors'])

    return returner_df


url = 'https://www.penguin.co.uk/articles/2018/100-must-read-classic-books/'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
results = extract_books_from_result(soup)
print(results)