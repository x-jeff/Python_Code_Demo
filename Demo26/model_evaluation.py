import pandas as pd
import statsmodels.api as sm

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

X = house[["SqFt", "Bedrooms", "Bathrooms", "Offers", "Yes", "East", "North"]]
Y = house["Price"].values
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2)
est2 = est.fit()
print(est2.summary())

# cal AIC
import itertools

predictorcols = ["SqFt", "Bedrooms", "Bathrooms", "Offers", "Yes", "East", "North"]
AICs = {}
for k in range(1, len(predictorcols) + 1):
    for variables in itertools.combinations(predictorcols, k):
        predictors = X[list(variables)]
        predictors2 = sm.add_constant(predictors)
        est = sm.OLS(Y, predictors2)
        res = est.fit()
        AICs[variables] = res.aic

from collections import Counter

c = Counter(AICs)
print(c.most_common()[::-10])

for variables in itertools.combinations(predictorcols, 2):
    print(variables)
