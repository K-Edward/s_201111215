
import os
import requests
import mylib
import json

_url='http://openAPI.seoul.go.kr:8088'
keyPath = os.path.join(os.getcwd(),'src', 'key.properties')
key = mylib.getKey(keyPath)
_key = str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_maxIter=2
_iter=0

#_api = _url+"/"+_key+"/"+_type+"/"+_service+"/"+str(_start_index)+"/"+ str(_end_index)+"/"+_use_mon+"/"

while _iter<_maxIter:
    _api = _url+"/"+_key+"/"+_type+"/"+_service+"/"+str(_start_index)+"/"+ str(_end_index)+"/"+_use_mon+"/"
    #print _api
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1

# data=requests.get(_api).text

# print data

# jd = json.loads(data)

# print jd

# print jd['SearchSTNBySubwayLineService']['row'][0]
# #n=len(jd['SearchSTNBySubwayLineService']['row'])
# #for i in range(0,n):
# #    print jd['SearchSTNBySubwayLineService']['row'][i]
# for item in jd['SearchSTNBySubwayLineService']['row']:
#     print item.keys()
#     for i in item.keys():
#         if i=='STATION_NM':
#             print ''.join(item.values())
#             print item.values()[1]