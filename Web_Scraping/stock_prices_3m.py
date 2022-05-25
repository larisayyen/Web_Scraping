
import numpy as np
import pandas as pd
import requests

# company stock prices in 3 months?
def fix_datetime(df):
    df['date']=pd.to_datetime(df['date'])
    df.set_index('date',inplace=True)

def create_stock_df(company_code):
    url = f"https://iex.lewagon.com/stable/stock/{company_code}/chart/3m"
    df = pd.read_json(url)
    fix_datetime(df)
    df['key'] = company_code
    return df

def normalize(series):
    return series/series[0]

# create stock csv of 4 companies
codes = ['aapl','amzn', 'googl', 'fb']
stock_dfs = []
for i in codes:
    stock_dfs.append(create_stock_df(i))

stocks = pd.concat(stock_dfs)
stocks.to_csv('raw_data/stocks.csv')

# normalize a pivot df
pivot_df = stocks.pivot(columns = 'key',values = 'close')
normalized_df = pivot_df.apply(normalize,axis = 0)
normalized_df.to_csv('raw_data/normalized.csv')
