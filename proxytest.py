#coding:utf-8
import requests
import json
import sys
ip = sys.argv[1]
port = sys.argv[2]
header ={'Proxy-Connection':'Keep-Alive'}
proxies={
    'http':'http://%s:%s'%(ip,port),
    'https':'http://%s:%s'%(ip,port)
}
r = requests.get('http://www.turing.click/test/index.htm',proxies=proxies,headers=header)
r.encoding='utf-8'
print r.text
