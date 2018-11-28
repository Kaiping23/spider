#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib,request

url='https://www.baidu.com'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.10 Safari/537.36"

}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

print(response)

# 数据处理

with open('simple.html','wb') as f:
    f.write(response.read())




