
import numpy as np
import pandas as pd
import requests

#last 3 months of Apple stock price
url = "https://iex.lewagon.com/stable/stock/aapl/chart/3m"

api_data = requests.get(url).json()
apple_df = pd.DataFrame(api_data)

apple_df['date'] = pd.to_datetime(apple_df['date'])
apple_df.set_index('date',inplace=True)
