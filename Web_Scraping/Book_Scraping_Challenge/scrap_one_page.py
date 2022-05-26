
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

#preparation

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
books = soup.select('article.product_pod')

#rating function

def book_rating(rating):
    rating_dict = {
    'One':1,'Two':2,'Three':3,'Four':4,'Five':5
}
    if rating[1] in rating_dict.keys():
        return rating_dict.get(rating[1],0)

#scrap one page

books_dict = {
    'Title':[],
    'Price':[],
    'Rating':[]
    }

for book in books:
    title = book.select_one('h3 a').attrs['title'].strip()
    price = float(book.select_one('div.product_price p').text[1:])
    rating = book_rating(book.select_one('p.star-rating').attrs['class'])

    books_dict['Title'].append(title)
    books_dict['Price'].append(price)
    books_dict['Rating'].append(rating)

book_df = pd.DataFrame.from_dict(books_dict)
book_df.to_csv('raw_data/book_df.csv')
