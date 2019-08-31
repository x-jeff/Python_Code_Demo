import json
import pandas
import xml.etree.ElementTree as ET

##json

with open ('jd.json','r') as f:
    jd=f.read()
#print(jd)

dic = json.loads(jd)
#print(dic)

jd2=json.dumps(dic)
#print(jd2)

df=pandas.read_json('jd.json')
#print(df)

##xml

tree=ET.parse('china.xml')#从xml文件中返回ElementTree
root=tree.getroot()
for city in root.iter('city'):
    print(city.get('cityname'),city.get('tem1'))
print(root.tag)
print(root.attrib)
for xx in root :
    print(xx.tag,xx.attrib)