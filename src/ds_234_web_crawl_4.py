# coding: utf-8

##노래제목 검색 후 crawl
##naver music에서 검색

import urllib
import re
import lxml.html
from lxml.cssselect import CSSSelector
import requests

search_Key = '목요일'

infomation = urllib.urlopen('http://music.naver.com/search/search.nhn?query=' + search_Key + '&x=0&y=0')
request = requests.get('http://music.naver.com/search/search.nhn?query=' + search_Key + '&x=0&y=0')

data = infomation.read()

##naver music에서 금요일 검색후 F12눌러보면 summary = "트랙 리스트"를 기준으로 곡 테이블이 나옴
##그 아래 tbody, 아래 class="_tracklist_move data1" 인 tr 아래 class = "name"인 td 에 곡명이 표현되어 있음
##class = "_title title NPI=" 인 href의 title에 곡명.
##class = "_artist artist" 인 td아래 href의 title이 가수명
##class = "album" 인 td 아래 href의 title이 앨범명

##regex 사용하기

key = data.find("트랙 리스트")
# if(key>0):
#     key = data.find("_title title NPI=", key)
#     key = data.find("title=", key+15)
#     key2 = data.find("\"", key+8)
#     print "---", data[key+7:key2]
# print len(data)

##제목 하나 가져오기 ↑

key = re.compile('title=".*목요일.*"')
respon = key.findall(data)
for item in respon:
    print item
    
print "===================================================================================="
print "===================================================================================="

##CSS selector 사용하기

##우선 제목만 찾아보기

html = lxml.html.fromstring(data)
html2 = lxml.html.fromstring(request.text)

select_title = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')

base = select_title(html)

for node in base:
    print node.text_content()

print "===================================================================================="
##제목,가수명,앨범 까지 모두 찾기

sel = CSSSelector('table[summary] > tbody > ._tracklist_move') ##공통부분까지는 동일하게 읽고
nodes = sel(html2)

##나뉘는 부분에서 각각 찾아감
select_song = CSSSelector('.name > a.title')
select_artist = CSSSelector('._artist.artist')
select_album = CSSSelector('.album > a')

for node in nodes:
    song = select_song(node)
    artist = select_artist(node)
    album = select_album(node)
    if song:
        print artist[0].text_content().strip()

        print song[0].text_content()

        print album[0].text_content()

        print "----------------------------------------"