import numpy as np
import pandas as pd

#使用np.nan表示缺失值
print(np.nan)

#构建一组含有缺失值的数据
df=pd.DataFrame([["Tim","M",24,169,100],["Jack","M",np.nan,177,140],["Jessy","F",21,162,np.nan],["Mary","F",23,159,87]])
#赋予列名
df.columns=["Name","Gender","Age","Height","Weight"]
print(df)

#判断是否存在缺失值
#检查第1行是否存在缺失值
print(df.loc[0].isnull().values.any())#返回False说明无缺失值
print(df[0:1].isnull().values.any())#另一种表达方式，也是检查第1行是否有缺失值
#检查第3列是否存在缺失值
print(df["Age"].isnull().values.any())#返回True说明存在缺失值
#判断整个DataFrame中是否存在缺失值
print(df.isnull().values.any())#返回True说明DataFrame中存在缺失值

#判断缺失值的具体位置
#判断第4行缺失值的具体位置
print(df.loc[3].isnull())#False为非缺失值，True为缺失值
print(df.loc[3].notnull())#False为缺失值，True为非缺失值
#判断第5列缺失值的具体位置
print(df["Weight"].isnull())
print(df["Weight"].notnull())
#判断整个DataFrame中是否存在缺失值
print(df.isnull())
print(df.notnull())
#同时检查所有列是否存在缺失值
print(df.isnull().any())

#统计缺失值的数量
#统计第2行缺失值的数量
print(df.loc[1].isnull().sum())
#统计第3列缺失值的数量
print(df["Age"].isnull().sum())
#整个DataFrame缺失值的数量
print(df.isnull().sum())#按列统计
print(df.isnull().sum().sum())#总计