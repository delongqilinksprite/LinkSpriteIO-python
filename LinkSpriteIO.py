#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File test.py

import urllib
import urllib2
import json
import time

deviceID="0000000xxx"
apikey = "89d20a92-6ecd-4f0a-a147-xxxxxxxxxxxx"
    
def http_post(data): 
    url = 'http://www.linksprite.io/api/http' 
    jdata = json.dumps(data)
    req = urllib2.Request(url, jdata)
    req.add_header('Content-Type','application/json') 
    response = urllib2.urlopen(req) 
    return response.read() 

def main():        
    tem = 123
    pre = 234
    values ={
    "action":"update",
    "apikey":apikey,
    "deviceid":deviceID,
    "params":
    {
        "EN-MG":tem,
        "FIR":pre
    }} 
    print http_post(values)
    print "--------------------------------"
    datas = {
    "action":"query",
    "apikey":apikey,
    "deviceid":deviceID,
    "params":
    [
        "EN-MG"    
    ]}
    print http_post(datas)
    print "---------------------------------"

if __name__=='__main__':
    main()
