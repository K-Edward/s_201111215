# coding: utf-8

##먼저 python 을 구글에 검색한 결과를  crawl 할 예정
##그냥 crawl -> user_Agent 변경 후 crawl

import urllib2
import os
import re

##google 검색창에 python 이라는 search 키워드를 검색하기 위해 주소(address) 생성
search_Key = 'python' ## 검색 결과에 한글이 포함되면 깨지는 현상 때문에 영문 결과가 예상되는 검색어를 지정
address = 'https://www.google.com/search?q=' + search_Key

##만든 주소를 바로 긁어오기 전 header의 user_Agent를 바꿔줘야 함
##header는 dictionary구조(?)
##python 프로그램에서 크롤링하면 제대로 된 정보를 크롤링 할 수 없음
##user-Agent를 웹브라우저처럼 가면(?)을 쓰고 접근.
header = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'}
request = urllib2.Request(address, None, header)
response = urllib2.urlopen(request)

crawl = response.read()
##print data ##확인용 print

##확인겸 html파일 만들어 보기

##f = open(os.path.join('src','mygoogle3.html'),'w')
##f.write(data)
##f.close()

## 파일 잘 만들어 진 것을 확인함 (google 검색창에 python이 검색된 페이지 만들어짐)

## 검색 결과 페이지에서 https://www.python 이 들어가는(유용하다고 판단한) 모든 링크를 가져오기

find = re.compile('href="(https://www.python.*?)"')
result = find.findall(crawl)

for data in result:
    print data