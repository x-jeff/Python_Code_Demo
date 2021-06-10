import pandas as pd

m_cols = ["Time", "Action", "User", "Product", "Quantity", "Price"]
orders = pd.read_csv("purchase_order.tab", sep='\t', parse_dates={'Dates': [0]}, names=m_cols, encoding='utf-8')
print(orders.info())
print(orders.head())
print(orders["Product"].head())
print(orders[orders["Product"] == "P0006944501"]["Price"].mean())
print(orders[orders["Product"] == "P0006944501"]["Price"].max())
print(orders[orders["Product"] == "P0006944501"]["Price"].min())
print(orders[orders["Product"] == "P0006944501"]["Price"].describe())
print(orders["Product"].unique())
print(len(orders["Product"].unique()))
print(orders.groupby("Product")["Price"].mean().head())
print(orders.groupby("Product")["Price"].mean().sort_values(ascending=False).head())
orders["Total_Price"] = orders["Quantity"] * orders["Price"]
print(orders.head())
print(orders.groupby('User')['Total_Price'].sum().sort_values(ascending=False).head())

m_cols = ['Time', 'Action', 'User', 'Product']
views = pd.read_csv("purchase_view.tab", sep='\t', parse_dates={"Dates": [0]}, names=m_cols, encoding='utf-8')
print(views.info())
print(orders.groupby(['User', 'Product'])['Product'].count().head())
orders_cnt = orders.groupby(['User', 'Product'])['Product'].count().reset_index(name='buys')
print(orders_cnt.head())
views_cnt = views.groupby(['User', 'Product'])['Product'].count().reset_index(name='views')
print(views_cnt.head())

merge_df = pd.merge(orders_cnt, views_cnt, on=['User', 'Product'], how='right')
print(merge_df.head())

merge_df = pd.merge(orders_cnt, views_cnt, on=['User', 'Product'], how='right')
print(merge_df.head())

print(views["Dates"].dt.date.head())
views_cnt_by_date = views.groupby(views["Dates"].dt.date)['Action'].count()
print(views_cnt_by_date.head())

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

views_cnt_by_date.plot(kind="line", figsize=[10, 5])
plt.show()

views_cnt_by_hour = views.groupby(views["Dates"].dt.hour)['Action'].count()
views_cnt_by_hour.plot(kind="line", title="view count by hour", figsize=[10, 5])
plt.show()

g = orders.groupby('User')['Total_Price'].sum().sort_values(ascending=False)[0:10]
g.plot(kind='bar', figsize=[10, 5])
plt.show()

view_daily_cnt = views.groupby(views["Dates"].dt.date)["Action"].count()
orders_daily_cnt = orders.groupby(orders["Dates"].dt.date)["Action"].count()
df = pd.concat([view_daily_cnt, orders_daily_cnt], axis=1)
df.dropna(inplace=True)
df.plot(kind="line", figsize=[10, 5], rot=30)
plt.show()
