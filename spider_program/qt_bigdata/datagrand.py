# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm
@time:2017/8/28 13:52
说明：下载 达观微信排行榜数据
http://www.datagrand.com/top/app_all_0_1.html
"""

import requests,json,time
# from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    'referer': "http://www.datagrand.com/top/app_1_0_1.html",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8"
    }

def getHtmlText(url,start,number):
  try:
    querystring = {"start":str(start),"number":str(number),"isapi":"1"}
    r = requests.get(url,headers=headers,params=querystring)
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return

def getdata(lst,html):
  for item in json.loads(html)['app_list']:
    row = []
    for v in item.values():
      if isinstance(v,list):
        v = str(v)
      row.append(v)
    lst.append(row)
  colname = item.keys()
  return colname

def main():
  data = []
  for i in range(4):
    url = 'http://www.datagrand.com/top/app_all_0_1.html'
    start = 25*i
    number = start + 29
    html = getHtmlText(url,start,number)
    colname = getdata(data,html)
    time.sleep(2)
  pd.DataFrame(data,columns=colname).to_csv('datagrand.csv',index=False,encoding='utf-8')

if __name__ == '__main__':
  main()

