# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

@author GengYanpeng
@software:PyCharm
@time:2017/8/4 14:14
功能：获取人人影院中，电影的 ed2k
"""

import os,time
import requests
from bs4 import BeautifulSoup

url = "http://oabt06.com/"

querystring = {"topic_title3":"纸牌屋","p":"3"}

headers = {
    # 'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # 'referer': "http://oabt06.com/?topic_title3=%E7%BA%B8%E7%89%8C%E5%B1%8B",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "PHPSESSID=im71mdq3nmt63h0g8qbucfkk94",
    'cache-control': "no-cache",
    # 'postman-token': "ef10aef7-be1a-5fcc-7fc8-281a126be325"
    }

r= requests.request("GET", url, headers=headers, params=querystring)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,'lxml')
dds = soup.select('body > div.middle-box > div > dl')[0]('dd')
urls = []
for dd in dds:
  try:
    url = dd.select('span.b > a')[0]['href']
    urls.append('http://oabt06.com' + url)
  except:
    print(dd.select('span.b > a'))
    continue

links = []
for url in urls:
  r = requests.get(url,headers=headers)
  soup = BeautifulSoup(r.text,'lxml')
  link = soup.select('body > div.middle-box > div > div.desc-box > div:nth-of-type(3) > p > a')[0]['href']
  if 'mkv' in link:
    continue
  links.append(link)
  print(link)


path = 'C:/Users/qt_52/Desktop/ed2k.txt'
path = '/Users/gengyanpeng/Downloads/ed2k.txt'
with open(path,'w+',encoding='utf-8') as f:
  for url in links:
    f.write(url+'\n')




