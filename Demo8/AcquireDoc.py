import requests
newsurl='http://news.qq.com/'
res=requests.get(newsurl)
print(res.text)