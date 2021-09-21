import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house-prices.csv")
print(df.head())

house = pd.concat([df, pd.get_dummies(df['Brick']), pd.get_dummies(df['Neighborhood'])], axis=1)
print(house.head())
del house['No']
del house['West']
del house['Brick']
del house['Neighborhood']
del house['Home']
print(house.head())

regr = LinearRegression()
X = house[["SqFt", "Bedrooms", "Bathrooms", "Offers", "Yes", "East", "North"]]
Y = house["Price"].values
regr.fit(X, Y)
regr.predict(X)
print(regr.predict(X))
