import pandas as pd
import numpy as np

print("*********读入数据*********")
df = pd.read_csv("student.csv", index_col=0)
# df=pd.read_csv("student.csv",na_values="NoData",index_col=0)
print(df)

print("*********查看前3行数据*********")
print(df.head(3))

print("*********处理缺失值*********")
df.loc[df["Height"] == "NoData", "Height"] = np.nan
print(df)

print("*********查看DataFrame信息*********")
print(df.info())

print("*********查看DataFrame列标签*********")
print(df.columns)

print("*********查看DataFrame字段类型*********")
print(df.dtypes)

print("*********查看DataFrame叙述性统计信息*********")
print(df.describe())

print("*********查看Grade字段*********")
print(df["Grade"].value_counts())
print(df[df["Grade"] == 3])

print("*********筛选字段*********")
print(df.loc[(df["Score"] > 90) & (df["Grade"] == 3)])

print("*********保存DataFrame*********")
df.to_csv("result.csv", index_label="Index")
