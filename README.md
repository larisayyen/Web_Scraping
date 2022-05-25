
# Data Sourcing - PART 1

Web Scraping and API are important data sourcing skills.

I use request.get() to scrap stock market information and use pandas to output csv.

```bash

api_data = requests.get(url).json()
df = pd.DataFrame(api_data)
df.to_csv()

```

In the tests folder, I also build up a function to test my results.
