import pandas as pd

df = pd.read_excel("house_price_regression.xlsx")
print(df.head(10))

df["age"] = df["age"].map(lambda e: 2021 - int(e.strip().strip('建筑年代：').strip('_x000D_\n')))  # 'age'列改为距今多少年
df[['room', 'living_room']] = df['layout'].str.extract('(\d+)室(\d+)厅')  # 抽取"室"和"厅"的数量
df['room'] = df['room'].astype(int)
df['living_room'] = df['living_room'].astype(int)
df['total_floor'] = df['floor_info'].str.extract('共(\d+)层')  # 提取总楼层数
df['total_floor'] = df['total_floor'].astype(int)
df['floor'] = df['floor_info'].str.extract('^(.)层')  # 抽取"高、中、低"层
df['direction'] = df['direction'].map(lambda e: e.strip().strip('_x000D_'))
del df['layout']
del df['floor_info']
del df['title']
del df['url']
df = pd.concat([df, pd.get_dummies(df['direction']), pd.get_dummies(df['floor'])], axis=1)  # 创建哑变量
del df['南北向']
del df['低']
del df['direction']
del df['floor']
del df['Unnamed: 0']
print(df.head())

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df[['price', 'area']].plot(kind='scatter', x='area', y='price', figsize=[10, 5])
plt.show()

from sklearn.linear_model import LinearRegression
import numpy as np

y = np.array(df['price']).reshape(-1, 1)
X = np.array(df['area']).reshape(-1, 1)
regr = LinearRegression()
regr.fit(X, y)
print('Coefficient:{}'.format(regr.coef_))
print('Intercept:{}'.format(regr.intercept_))
plt.scatter(X, y, color='blue')
plt.plot(X, regr.predict(X), linewidth=3, color='red')
plt.xlabel('area')
plt.ylabel('price')
plt.show()

y = df['price'].values
X = df[['age', 'area', 'room', 'living_room', 'total_floor', '东南向', '东向', '南向', '西南向', '西向', '中', '高']]
regr = LinearRegression()
regr.fit(X, y)
print(X.info())

import statsmodels.api as sm

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

predictorcols = ['age', 'area', 'room', 'living_room', 'total_floor', '东南向', '东向', '南向', '西南向', '西向', '中', '高']
import itertools

AICs = {}
for k in range(1, len(predictorcols) + 1):
    for variables in itertools.combinations(predictorcols, k):
        predictors = X[list(variables)]
        predictors2 = sm.add_constant(predictors)
        est = sm.OLS(y, predictors2)
        res = est.fit()
        AICs[variables] = res.aic
from collections import Counter

c = Counter(AICs)
print(c.most_common()[::-10])
