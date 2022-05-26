
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")

book_html = soup.select('article.product_pod')

#scrap one book : title,price

book = []
book.append(book_html[0].select_one('h3 a').attrs['title'].strip())
book.append(float(book_html[0].select_one('div.product_price p').text[1:]))

#scrap book rating

book_r = book_html[0].select_one('p.star-rating').attrs['class']

def book_rating(rating):
    rating_dict = {
    'One':1,'Two':2,'Three':3,'Four':4,'Five':5
}
    if rating[1] in rating_dict.keys():
        return rating_dict.get(rating[1],0)

r = book_rating(book_r)
book.append(r)

print(book)
