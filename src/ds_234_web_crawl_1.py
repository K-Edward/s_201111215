##requests 방식 사용

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import lxml.html
from lxml.cssselect import CSSSelector

resp = requests.get('http://python.org/')
htmlTxt = resp.text ## htmlTxt는 unicode

##regex
## http://로 시작하는 url 찾기
f_Item = re.compile('href="(http://.*?)"')
basket = f_Item.findall(htmlTxt)

for i, node in enumerate(basket):
    print i+1, node

## +추가) h1태그 찾아보기
print "==========<h1> 태그 찾아보기=========="

f_Tag = re.compile('<h1>(.*?)</h1>')
h1_Tag = f_Tag.findall(htmlTxt)

for tag in h1_Tag:
    print tag

print "======================================"
    
## +추가) p태그 찾아보기
print "================================<p> 태그 찾아보기==================================="

f_p_Tag = re.compile('<p>(.*?)</p>')
p_Tag = f_p_Tag.findall(htmlTxt)

for tag in p_Tag:
    print tag
    
print "===================================================================================="

##beautiful soup

## strong 태그 찾기

print "==========================strong 태그 찾기================================"

tree = BeautifulSoup(htmlTxt, "lxml")
strong_Tag = tree('strong')

for tag in strong_Tag:
    print tag
    
print "=========================================================================="

## div 태그 찾기

print "================================div 태그 찾기===================================="

tree = BeautifulSoup(htmlTxt, "lxml")
div_Tag = tree('div')
counter = 0

for tag in div_Tag:
    if counter == 1: ##첫 div는 내용이 너무 길어서 그 다음 div 태그를 찾아서 출력함.
        print counter, tag
    counter = counter + 1
    
print "================================================================================="

## xpath

print "==================================xpath 를 이용한 crawl============================"

html_Tree = etree.HTML(htmlTxt)
st_Html = etree.tostring(html_Tree, pretty_print=True, method = "html")

##아랫줄은 확인용 출력
##print st_Html[:500] ##내용이 길어 string 글자수 제한함

nodes = html_Tree.xpath('//*[@href]')

for k, node in enumerate(nodes):
    if k<10:
        print k+1,".", node.attrib  ##찾은 node 의 attribute를 10개만 출력함.
        
print "==================================================================================="


## CSS Selector

print "=================================CSS Selector 사용================================="

addr = requests.get('http://python.org/')
html_Str = lxml.html.fromstring(addr.text)

selector = CSSSelector('a[href]')
nodes = selector(html_Str)

for g, node in enumerate(nodes):
    if g<10:
        print g+1,".", node.get('href'), node.text
        
print "==================================================================================="