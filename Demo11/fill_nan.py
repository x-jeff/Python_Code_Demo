import pandas as pd
import numpy as np

df=pd.DataFrame([["Tim","M",24,169,100],["Jack","M",np.nan,177,np.nan],["Jessy","F",21,162,np.nan],["Mary","F",23,159,87]])
df.columns=["Name","Gender","Age","Height","Weight"]
df["Salary"]=np.nan
print(df)

#使用数值2填补缺失值
print(df.fillna(2))

#使用平均值填补缺失值
df["Age"].fillna(df["Age"].mean())
print(df)
df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)

np.random.seed(1)
df=pd.DataFrame({"key1":list('aabba'),"key2":["one","two","one","two","one"],"data1":np.random.randn(5),"data2":np.random.randn(5)})
print(df)

#求分层平均数
grouped=df["data1"].groupby(df["key1"])
print(grouped.mean())
# df["data1"]=df["data1"].groupby(df["key1"]).transform("mean")#方法一
df["data1"]=df.groupby("key1")["data1"].transform("mean")#方法二
print(df)

df=pd.DataFrame([["Tim","M",24,169,100],["Jack","M",np.nan,177,np.nan],["Jessy","F",21,162,np.nan],["Mary","F",23,159,87],["Jim","M",23,np.nan,np.nan]])
df.columns=["Name","Gender","Age","Height","Weight"]
df["Salary"]=np.nan
print(df)
#用各性别年龄平均值填补缺失值
#方式一
df["Age"].fillna(df["Age"].groupby(df["Gender"]).transform("mean"),inplace=True)
print(df)
#方式二
df["Age"].fillna(df.groupby("Gender")["Age"].transform("mean"),inplace=True)
print(df)

df=pd.DataFrame([["Tim","M",24,169,100],["Jack","M",np.nan,177,np.nan],["Jessy","F",21,162,np.nan],["Mary","F",23,159,87],["Jim","M",23,np.nan,np.nan]])
df.columns=["Name","Gender","Age","Height","Weight"]
print(df)
#向后填补缺失值
# df.fillna(method="pad",inplace=True)
# print(df)
#向前填补缺失值
# df.fillna(method="bfill",inplace=True)
# print(df)
#在向前填补缺失值时，只填补一行
df.fillna(method="bfill",inplace=True,limit=1)
print(df)

df=pd.DataFrame([[1,870],[2,900],[np.nan,np.nan],[4,950],[5,1000],[6,1200]])
df.columns=["Time","Value"]
print(df)
#使用内插法填补缺失值
print(df.interpolate())