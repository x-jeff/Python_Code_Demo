import pandas as pd
df=pd.DataFrame([['Frank','M',29],['Mary','F',23],['Tom','M',35],['Ted','M',33],['Jean','F',21],['Lisa','F',20]])
df.columns=['Name','Gender','Age']
print(df)
print(df.loc[0:3])
print(df.iloc[0:3])
print(df[df['Gender']=='M'])
print(df['Gender']=='M')
print(df[df['Gender']!='M'])
print(df[(df['Gender']=='F') & (df['Age']>=21)])
print(df[(df['Gender']=='F') | (df['Age']>22)])
df['Employee']=True
print(df)
df['Level']=[1,2,3,4,5,6]
print(df)
#df.loc[6]={'Name':'Wade','Gender':'M','Age':28,'Employee':True,'Level':7}
df.loc[6]=['Wade','M',28,True,7]
print(df)
df = df.append(pd.DataFrame([{'Name':'James','Gender':'M','Age':32,'Employee':True,'Level':8}]),ignore_index=True,sort=False)
# df = df.append(pd.DataFrame([{'Name':'James','Gender':'M','Age':32,'Employee':True,'Level':8}]),ignore_index=False,sort=True)
print(df)
# del df['Employee']
# print(df)
df = df.drop('Employee',1)
print(df)
df = df.drop(7,0)
print(df)
df['UserID']=range(101,108)
df.set_index('UserID',inplace=True)
print(df)