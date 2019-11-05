from bs4 import BeautifulSoup
html_sample='\
<html>\
<body>\
<h1 id="title">Hello World</h1>\
<a href="#" class="link">This is link1</a>\
<a href="# link2" class="link">This is link2</a>\
</body>\
</html>'
soup=BeautifulSoup(html_sample,'html.parser')
print(soup.text)

header=soup.select('h1')
print(header)

alink=soup.select('a')
print(alink)

print(soup.select('h1')[0].text)
for xx in alink:
    print(xx.text)

alink=soup.select('#title')
print(alink)
for link in soup.select('.link'):
    print(link)

alinks=soup.select('a')
for link in alinks :
    print(link['href'])
    print(link['class'])
print(alinks[0]['href'])
print(alinks[0]['class'])