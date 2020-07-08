import pandas as pd
import numpy as np
df=pd.read_csv("house_price.csv")
pd.set_option('display.max_columns', None)
print(df.head())
print(df["总价"]*10000)
print(np.sqrt(df["总价"]))
print(df["朝向"]+df["户型"])
print(df["总价"] * 10000 / df["建筑面积"])
df["均价"]=df["总价"] * 10000 / df["建筑面积"]
print(df.head())

#Map用法
#移除物业费中的元
#方法一
def removeDollar(e):
    return e.split('元')[0]
df["物业费"].map(removeDollar)
print(df["物业费"].map(removeDollar))
#方法二：使用匿名函数
df["物业费"].map(lambda e:e.split('元')[0])
print(df["物业费"].map(lambda e:e.split('元')[0]))

#split用法举例
s="1.5元/平米.月"
print(s.split("元"))
print(s.split("元")[0])

#Apply用法
df2=pd.DataFrame([[60,70,50],[80,79,68],[63,66,82]],columns=["First","Second","Third"])
print(df2.head())
print(df2.apply(lambda e:e.max()-e.min(),axis=0))
print(df2.apply(lambda e:e.max()-e.min(),axis=1))

#ApplyMap用法
#将df中所有“暂无资料”的元素替代成缺失值
#方法一
def convertNaN(e):
    if e == "暂无资料":
        return np.nan
    else:
        return e
df=df.applymap(convertNaN)
#方法二
df=df.applymap(lambda e:np.nan if e=="暂无资料" else e)
print(df.head())