import pandas_datareader

df = pandas_datareader.data.DataReader('BABA', data_source='yahoo')
print(df.tail())
print(df.columns)

# 算出总和
print(df['Close'].sum())
# 算出平均
print(df['Close'].mean())
# 算出标准差
print(df['Close'].std())
# 取得最小值
print(df['Close'].min())
print(df[['Open', 'Close']].min())
# 取得最大值
print(df['Close'].max())
print(df[['Open', 'Close']].max())
# 取得笔数
print(df['Close'].count())

# 取得整体叙述性统计
print(df.describe())

# 计算当日涨跌
df['diff'] = df['Close'] - df['Open']
df['rise'] = df['diff'] > 0
df['fall'] = df['diff'] < 0
# 计算涨跌次数
print(df[['rise', 'fall']].sum())
# 计算当月涨跌次数
print(df.index)
print(df.loc[df.index >= '2017-04-01', ['rise', 'fall']].sum())
# 根据年月统计涨跌次数
print(df.index.year)
print(df.index.month)
print(df.groupby([df.index.year, df.index.month])['rise', 'fall'].sum())
# 计算每日报酬
df['ret'] = df['Close'].pct_change(1)
print(df['ret'])
