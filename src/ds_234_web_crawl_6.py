# coding: utf-8

import urllib2
import requests
import re
import lxml.etree

r = requests.get('http://www.kbreport.com/main')
html_Tree = lxml.etree.HTML(r.text)

nodes = html_Tree.xpath("//div[@class='team-rank-box']//table[@class='team-rank']//tr")
print u"테이블 행 갯수: ", len(nodes)
counter = 0
for teams in nodes:
    for cols in teams:
        if cols.xpath('.//a/text()'):
            print cols.xpath('.//a/text()')[0],
        else:
            print cols.text.strip(),
    print