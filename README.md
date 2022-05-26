
# Data Sourcing

Web Scraping and API are important data sourcing skills.

# Stock Market Challenge
use request.get() to scrap stock market information
use pandas to output csv

```bash

api_data = requests.get(url).json()
df = pd.DataFrame(api_data)
df.to_csv()

```

# Book Scraping Challenge
use BeautifulSoup to scrap book information
use select function to select books in html

```bash

url = 'http://books.toscrape.com/'
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")
books = soup.select('article.product_pod')

for book in books:
  title = book.select_one('h3 a').attrs['title'].strip()
  price = float(book.select_one('div.product_price p').text[1:])
  rating = book_rating(book.select_one('p.star-rating').attrs['class'])

```

# Test
build up test functions to check results

run the following command line in the terminal

```bash

make test

```
