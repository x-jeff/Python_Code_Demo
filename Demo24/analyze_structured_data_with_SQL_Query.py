import pandas as pd
import sqlite3 as lite

df = pd.read_csv("Region_Data.csv", encoding='gb2312', skiprows=3, skipfooter=2, engine="python")
print(df)

df = pd.melt(df, col_level=0, id_vars="地区")
print(df)

df['variable'] = df['variable'].map(lambda e: int(e.strip('年')))
print(df)

df.columns = ['area', 'year', 'gross_product']
print(df)

with lite.connect('country_stat.sqlite') as db:
    df.to_sql('regional_gross_product', con=db, if_exists='replace', index=None)

with lite.connect('country_stat.sqlite') as db:
    df2 = pd.read_sql('SELECT * FROM regional_gross_product', con=db)
    print(df2.head())
    df2 = pd.read_sql('SELECT area,gross_product FROM regional_gross_product', con=db)
    print(df2.head())
    df2 = pd.read_sql('SELECT * FROM regional_gross_product WHERE year=2014', con=db)
    print(df2.head())

with lite.connect('country_stat.sqlite') as db:
    df3 = pd.read_sql('SELECT * FROM regional_gross_product ORDER BY gross_product DESC', con=db)
    print(df3.head())
    df3 = pd.read_sql('SELECT * FROM regional_gross_product ORDER BY gross_product DESC LIMIT 3', con=db)
    print(df3.head())

with lite.connect('country_stat.sqlite') as db:
    df4 = pd.read_sql(
        'SELECT area,AVG(gross_product) as avg_gross_product FROM regional_gross_product GROUP BY area HAVING avg_gross_product >= 10000',
        con=db)
    print(df4.head())
