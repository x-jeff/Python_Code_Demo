import requests

payload = {'startDate': '2021-05-01', 'endDate': '2021-08-01', 'queryYN': 'true'}
res = requests.post('http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do', data=payload)
print(res)
# print(res.text)

from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)  # 将模糊字符宽度设置为2
pd.set_option('display.unicode.east_asian_width', True)  # 检查东亚字符宽度属性

soup = BeautifulSoup(res.text, 'html.parser')
dfs = pd.read_html(soup.select('#InfoTable')[0].prettify('utf-8-sig'), header=0)
df_rates = dfs[0]
print(df_rates.head())

df_rates = pd.melt(df_rates, col_level=0, id_vars=['日期'])
df_rates.columns = ['date', 'currency', 'exchange']
print(df_rates.head())

import sqlite3 as lite

with lite.connect('currency.sqlite') as db:
    df_rates.to_sql('currency_data', con=db, if_exists='replace', index=None)

from datetime import datetime, timedelta

current_time = datetime.now()
for i in range(1, 5 * 366, 366):
    start_time = (current_time - timedelta(days=i + 366)).strftime('%Y%m%d')
    end_time = (current_time - timedelta(days=i + 1)).strftime('%Y%m%d')
    print(start_time, end_time)

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

with lite.connect('currency.sqlite') as db:
    df = pd.read_sql("SELECT * FROM currency_data WHERE currency='美元'", con=db)
    print(df.head())
    # print(df.info())
    # df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
    # print(df.head())
    # print(df.info())
    # df.index = df.date
    # print(df.head())
    # df['exchange'].plot(kind='line')
    # plt.show()

with lite.connect('currency.sqlite') as db:
    df = pd.read_sql("SELECT * FROM currency_data WHERE currency IN ('美元','英镑')", con=db)
    print(df)
    df.currency.unique()
    # print(df)
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
    df2 = df.pivot_table(index='date', columns='currency')
    print(df2)
    df2.plot(kind='line', rot=90)
    plt.show()
