import pandas as pd
import re

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('expand_frame_repr', False)  # 禁止自动换行
# 下面两个语句用于列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_csv("../Demo14/house_price.csv")
print(df)

df[['室', '厅', '厨', '卫']] = df['户型'].str.extract('(\d+)室(\d+)厅(\d+)厨(\d+)卫', expand=True)
print(df)

