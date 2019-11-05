from bs4 import BeautifulSoup
import requests
import pandas

PriceUrl='https://newhouse.fang.com/house/s/'
res=requests.get(PriceUrl)
res.encoding='gb2312'
#print(res.text)

housedf=pandas.DataFrame()
soup=BeautifulSoup(res.text,'html.parser')

rows=1
for house_name in soup.select('.nlcd_name'):
    housedf.loc[rows,'house_name']=house_name.text.strip()
    rows+=1

rows=1
for house_url in soup.select('.nlcd_name a'):
    housedf.loc[rows,'house_url']='https:' + house_url['href']
    rows+=1

rows=1
for house_price in soup.select('.nhouse_price'):
    housedf.loc[rows,'house_price']=house_price.text.strip()
    rows+=1

pandas.set_option('display.max_columns', None) #显示所有的列
pandas.set_option('max_colwidth',45) #设置列宽
print(housedf)

