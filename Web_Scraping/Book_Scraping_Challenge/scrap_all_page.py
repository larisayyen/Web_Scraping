
import requests
import pandas as pd
from bs4 import BeautifulSoup

#rating function

def book_rating(rating):
    rating_dict = {
    'One':1,'Two':2,'Three':3,'Four':4,'Five':5
}
    if rating[1] in rating_dict.keys():
        return rating_dict.get(rating[1],0)

#scrap all pages

def scrap_all(PAGES):

    all_books={'Title': [], 'Price': [], 'Rating': []}

    for page in range(1,PAGES+1):
        url = f'http://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')

        all_books_html = soup.select('article.product_pod')

        for book in all_books_html:
            title = book.select_one('h3 a').attrs['title'].strip()
            price = float(book.select_one('div.product_price p').text[1:])
            rating = book_rating(book.select_one('p.star-rating').attrs['class'])

            all_books['Title'].append(title)
            all_books['Price'].append(price)
            all_books['Rating'].append(rating)

    df = pd.DataFrame.from_dict(all_books)

    return df

df = scrap_all(50)
df.to_csv('raw_data/50_page.csv')
