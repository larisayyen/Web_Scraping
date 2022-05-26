
from urllib import request
import requests
import pandas as pd

symbol_to_test = ['fb','aapl','amzn', 'googl','tsla']

# market cap?
def stats_info(symbol):
    url = f"https://iex.lewagon.com/stable/stock/{symbol}/stats"
    api_data = requests.get(url).json()
    return api_data.get('marketcap')

# research and development spendings quarterly?
def spending_info(symbol):
    url=f"https://iex.lewagon.com/stable/stock/{symbol}/financials"
    api_data = requests.get(url).json()
    return api_data.get('financials')[0].get('researchAndDevelopment','Fail to scrap')

# Most recent news?
def recent_news(symbol,num):
    url = f"https://iex.lewagon.com/stable/stock/{symbol}/news/last/{num}"
    api_data = requests.get(url).json()
    new_df = pd.DataFrame(api_data)
    return new_df

# Sector performance?
def sector_perform():
    url = "https://iex.lewagon.com/stable/stock/market/sector-performance"
    api_data = requests.get(url).json()
    new_df = pd.DataFrame(api_data)
    return new_df

# test

# print(stats_info('fb'))
# print(spending_info('aapl'))

# recent_news('tsla',1).to_csv('raw_data/tsla_news.csv')
# sector_perform().to_csv('raw_data/sector.csv')
