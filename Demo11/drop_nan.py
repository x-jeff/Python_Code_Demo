import pandas as pd
import numpy as np

df=pd.DataFrame([["Tim","M",24,169,100],["Jack","M",np.nan,177,np.nan],["Jessy","F",21,162,np.nan],["Mary","F",23,159,87]])
df.columns=["Name","Gender","Age","Height","Weight"]
df["Salary"]=np.nan
print(df)

#舍弃含有缺失值的行/列
#舍弃含有缺失值的行
print(df.dropna(axis=0,how="any"))#默认参数
#舍弃含有缺失值的列
print(df.dropna(axis=1,how="any"))

#舍弃全部为缺失值的行/列
#以列为例：axis=1
print(df.dropna(axis=1,how="all"))

#仅保留非缺失值数量大于等于一定阈值的行/列
#以行为例：axis=0
print(df.dropna(axis=0,thresh=4))