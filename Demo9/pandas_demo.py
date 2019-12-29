import pandas as pd
df=pd.DataFrame([['Frank','M',29],['Mary','F',23],['Tom','M',35],['Ted','M',33],['Jean','F',21],['Lisa','F',20]])
#print(df)
df.columns=['name','gender','age']
#print(df)

type=pd.Series([21,18,35])
#print(type)
type=pd.Series([21,18,35],index=['A','B','C'])
#print(type)

#print(df.info())
print(df.describe())
print(df["age"].describe()['mean'])