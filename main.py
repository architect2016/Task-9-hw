import requests
from bs4 import BeautifulSoup
import json


urls = [f"http://quotes.toscrape.com/page/{page}" for page in range(1, 11)]


quotes = []
authors = []


for url in urls:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    quotes_on_page = soup.find_all('span', class_='text')
    authors_on_page = soup.find_all('small', class_='author')


    quotes.extend([quote.get_text() for quote in quotes_on_page])
    authors.extend([author.get_text() for author in authors_on_page])


with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump([{'quote': quote} for quote in quotes], f, ensure_ascii=False, indent=4)

with open('authors.json', 'w', encoding='utf-8') as f:
    json.dump([{'author': author} for author in authors], f, ensure_ascii=False, indent=4)