import pandas as pd

df = pd.read_csv("../Demo14/house_price.csv")
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)
# 列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)
print(df)

print(pd.get_dummies(df["朝向"]))

df = pd.concat([df, pd.get_dummies(df["朝向"])], axis=1)
print(df)

df = df.drop("朝向", axis=1)
print(df)

df2 = df.pivot_table(index="日期", columns="户型", values="总价", aggfunc='sum', fill_value=0)
print(df2)
print(df2.T)

df_multi_idx = df.pivot_table(index=["标题", "建筑面积"], columns="户型", values="总价", aggfunc='sum')
print(df_multi_idx)

df_wide = df_multi_idx.unstack()
print(df_wide)

df_long = df_wide.stack()
print(df_long)
