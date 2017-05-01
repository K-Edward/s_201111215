
import os
import src.mylib
import urlparse
import requests
import re
import lxml
import lxml.etree
import StringIO

keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
key = src.mylib.getKey(keyPath)
KEY = str(key['dataseoul'])
TYPE='xml'
SERVICE = 'SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(200)
LINE_NUM=str(1)

params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url1 = 'http://openAPI.seoul.go.kr:8088/'
url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))

print "*******************"
print "1호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"


LINE_NUM=str(2)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "2호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
LINE_NUM=str(3)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "3호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str(4)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "4호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    

LINE_NUM=str(5)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "5호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str(6)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "6호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str(7)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "7호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str(8)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "8호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str(9)
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "9호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str('I')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "인천 1호선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    

LINE_NUM=str('K')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "경의 중앙선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str('B')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "분당선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str('A')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "공항철도"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str('G')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "경춘선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str('S')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "신분당선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"
    
    
LINE_NUM=str('SU')
params = KEY + "/" + TYPE + "/" + SERVICE + "/" + START_INDEX + "/" + END_INDEX + "/" + LINE_NUM + "/"

url2 = urlparse.urljoin(url1, params)

data = requests.get(url2).text
    
tree = lxml.etree.fromstring(data.encode('utf-8'))
    
print "\n\n*******************"
print "수인선"
print "*******************"

nodes = tree.xpath('//STATION_NM')
for node in nodes:
    print node.text
    print "-------------------"