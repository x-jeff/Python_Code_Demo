import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def getArticle(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')
    dic = {}
    dic["title"] = soup.select(".main-title")[0].text
    dic["content"] = ''.join(soup.select(".article")[0].text.split())
    dic["source"] = soup.select(".date-source")[0].text
    dic["keywords"] = soup.select(".keywords")[0].get("data-wbkey")
    return dic


res = requests.get("https://news.sina.com.cn/china/")
# print(res.text)
# print(res.encoding)
res.encoding = 'utf-8'
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

news_soup = soup.select(".main-content .left-content-1.marBot ul")[1]
# print(news_soup)

num = 0
newsary = []
for link in news_soup.select('a'):
    num = num + 1
    n = 13
    if num > n and num < n + 5:  # 仅挑选部分新闻作为例子
        # print(link)
        newsary.append(getArticle(link["href"]))
# print(newsary)

df = pd.DataFrame(newsary)
# print(df)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)
# print(df)

# 整理文章关键词
df["keywords"] = df["keywords"].map(lambda e: e.split(","))
# print(df["keywords"])

# 整理文章来源
df[["datetime", "from"]] = df["source"].str.extract('\n+(\d+年\d+月\d+日 \d+:\d+)\n+(\w+)', expand=False)
# print(df)
# 转换datetime格式
df["datetime"] = pd.to_datetime(df["datetime"], format="%Y年%m月%d日 %H:%M")
# print(df["datetime"])
# print(df["datetime"].map(lambda e: e.year))  # 提取年份
# print(df["datetime"].map(lambda e: e.month))  # 提取月份
del df["source"]
# print(df)

# 调整栏位顺序
df = df[["from", "title", "content", "keywords", "datetime"]]
# print(df)

# 将整理好的数据存储至Excel
df.to_excel("news.xlsx")
