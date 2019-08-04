with open('demo.csv','r') as f:
    print(f.read())
import pandas
df=pandas.read_csv('demo.csv')
print(df)
#print(df[0])#error
#print(df[1])#error
print(df['name'])
print(df[0:3])
#print(df[0,2])#error
print(df.loc[0:3,'name'])
print(df.loc[0:2,'name':'score'])
print(df.iloc[0:3,0:2])
print(df.iloc[0,1])
print(df.iloc[[0,2,4]])
df_xls=pandas.read_excel('demo.xls')
print(df_xls)