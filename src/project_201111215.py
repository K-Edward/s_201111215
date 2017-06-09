# -*- coding: utf-8 -*- 
import urllib
import oauth2 as oauth
import json
import os
import sys

os.environ["SPARK_HOME"]="C:/Users/Administrator/Code/s_201111215/spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark

myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder\
    .master("local")\
    .appName("myApp")\
    .config(conf=myConf)\
    .config('spark.sql.warehouse.dir', 'file:///C:/Users/Administrator/Code/s_201111215/data')\
    .getOrCreate()


def getApiKey(keyPath):
    d = dict()
    f = open(keyPath, 'r')
    for line in f.readlines():
        row = line.split('=')
        if(row[0] != 'debug'):
            row0 = row[0].split('.')
            d[row0[1].upper()]=row[1].strip()
    return d

keyPath=os.path.join("C:/Users/Administrator/Code/s_201111215/src/twitter4j.properties")
key=getApiKey(keyPath)

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client = oauth.Client(consumer, token)

_fname='src/ds_twitter_weather.txt'

def saveFile(_fname,_data):
    fp=open(_fname,'a')
    fp.write(str(_data))

url = "https://api.twitter.com/1.1/search/tweets.json"
_ids=list()
_max_id=None
_count=100
_maxIter=20
_iter=0
while _iter<_maxIter:
    myparam={'q':'미세먼지','count':_count,'max_id':_max_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    #print len(tsearch_json)
    for i,tweet in enumerate(tsearch_json['statuses']):
            print tweet['text']
            saveFile(_fname,tweet['text'].encode('utf-8'))

    _max_id=tweet['id']
    print tweet['text']
    _ids.append(tweet['text'])
    _iter+=1

myRdd2 = spark.sparkContext.textFile(os.path.join("src", "ds_twitter_weather.txt"))

wc2=myRdd2\
    .flatMap(lambda x:x.split())\
    .map(lambda x:(x,1))\
    .take(10000)
    
for i in wc2:
    print i