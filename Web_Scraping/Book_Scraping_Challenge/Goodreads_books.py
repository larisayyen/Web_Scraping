
import requests
import pandas as pd
import numpy as np

# fetch url and subjects
def fetch_book_coverurl(isbn13):
    url='https://openlibrary.org/api/books'
    params={
        'bibkeys':f'ISBN:{isbn13}',
        'format':'json',
        'jscmd':'data'
    }
    res=requests.get(url,params=params).json()

    if f'ISBN:{isbn13}' in res:
        return res[f'ISBN:{isbn13}'].get('cover',{}).get('large','Not found')
    else:
        return None

def fetch_subjects(isbn13):
    url='https://openlibrary.org/api/books'
    params={
        'bibkeys':f'ISBN:{isbn13}',
        'format':'json',
        'jscmd':'data'
    }
    res=requests.get(url,params=params).json()
    if f'ISBN:{isbn13}' in res:
        sujects_l= res[f'ISBN:{isbn13}'].get('subjects',[])
        return sujects_l[0].get('name','Not found')
    else:
        return None

# iterate through 100 rows, add url and subjects to csv

df = pd.read_csv('raw_data/books.csv')
df['cover_url'] = None
df['subjects'] = None

for index , row in df.head(100).iterrows():
    if row['cover_url'] is None:
        cover_url =fetch_book_coverurl(row['isbn13'])
        print(f"fetching cover url for {row['title']}")
        if cover_url:
            df.loc[index,'cover_url'] = cover_url

for index,row in df.head(100).iterrows():
    if row['subjects'] is None:
        subjects=fetch_subjects(row['isbn13'])
        print(f"Fetching subjects for {row['title']}")
        if subjects:
            df.loc[index,'subjects']=subjects
