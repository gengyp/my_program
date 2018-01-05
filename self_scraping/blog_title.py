# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/8/26 23:38
http://blog.topspeedsnail.com/page/2

"""
import requests
from bs4 import BeautifulSoup
import time,os

file_path = 'WTF_Daily_Blog.txt'
if os.path.exists(file_path):
  os.remove(file_path)

for page in range(1,150):
  with open(file_path,'a+') as f:
    url = 'http://blog.topspeedsnail.com/page/' + str(page)
    print(url + '\n'+ '- '*20 ,file=f)
    r= requests.get(url)
    r.status_code
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'lxml')
    for tag in soup.select('#content h2 > a'):
      print(tag.text,file=f)
    print('*'*40,file=f)
    time.sleep(1)
  print('\rcur num is:',page,149,end='')