# Topical Clustering of News : 1
import requests
import json
from bs4 import BeautifulSoup
import pandas

def getArticle(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return ' '.join([p.text.strip() for p in soup.select('#article p')])

df = pandas.DataFrame()
for page in range(1, 11):
    url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2669&k=&num=50&page=' + str(
        page) + '&r=0.1534653757567701'
    res = requests.get(url)
    data = json.loads(res.content)

    ary = []
    for rec in data['result']['data']:
        try:
            ary.append({'title': rec['title'], 'url': rec['url'], 'content': getArticle(rec['url'])})
        except:
            print(rec['ext_3'])

    if df.empty:
        df = pandas.DataFrame(ary)
    else:
        df = df.append(pandas.DataFrame(ary), ignore_index=True)
df.to_excel('news.xlsx')
