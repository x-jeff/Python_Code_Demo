import pandas_datareader
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pandas_datareader.DataReader('BABA', data_source='yahoo', start='2020-05-01')
print(df.head())

df['Close'].plot(kind='line', figsize=[10, 5], title='BABA', legend=True, grid=True)
plt.show()

df['mvg30'] = df['Close'].rolling(window=30).mean()
df[['Close', 'mvg30']].plot(kind='line', legend=True, figsize=[10, 5])
plt.show()

df.loc[df.index >= '2021-05-01', 'Volume'].plot(x='datetime', kind='bar', figsize=[10, 5], title='BABA', legend=True)
plt.show()

df['diff'] = df['Close'] - df['Open']
df['rise'] = df['diff'] > 0
df['fall'] = df['diff'] < 0
df[['rise', 'fall']].sum().plot(kind='pie', figsize=[5, 5], counterclock=True, startangle=90, legend=True)
plt.show()
