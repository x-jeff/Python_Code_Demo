import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('salary.csv', index_col=0)
print(df.head())

X = df[['year']]
Y = df['salary'].values
plt.scatter(X, Y, color='black')
plt.xlabel('year')
plt.ylabel('salary')
plt.show()

regr = LinearRegression()
regr.fit(X, Y)
print('Coefficients:', regr.coef_)
print('Intercept:', regr.intercept_)

plt.scatter(X, Y, color='black')
plt.plot(X, regr.predict(X), color='blue', linewidth=3)
plt.show()

poly_reg = PolynomialFeatures(degree=2)
X_ = poly_reg.fit_transform(X)

regr = LinearRegression()
regr.fit(X_, Y)

X2 = X.sort_values(['year'])
X2_ = poly_reg.fit_transform(X2)

plt.scatter(X, Y, color='black')
plt.plot(X2, regr.predict(X2_), linewidth=3, color="blue")
plt.show()
