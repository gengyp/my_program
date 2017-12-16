# -*- coding:utf-8 -*-
"""
爬取 搜狐娱乐信息
"""
import requests
import json
import pymongo
import time
from multiprocessing import Pool

client = pymongo.MongoClient('localhost',27017,maxPoolSize=4)
weibo = client['weibo'] # 数据库，已存在则使用，不存在则创建
comments = weibo['comments'] # 建表

url = "https://m.weibo.cn/api/comments/show"
headers = {
  'upgrade-insecure-requests': "1",
  'x-devtools-emulate-network-conditions-client-id': "79a4d881-7214-4d72-9876-972730f00095",
  'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  'accept-encoding': "gzip, deflate, br",
  'accept-language': "zh-CN,zh;q=0.8",
  'cookie': "_T_WM=5758b102fbd0fa73d2804deaebaae298",
  'cache-control': "no-cache",
  # 'postman-token': "f8ff4f0b-8b95-1d8b-a5b3-ef68d6a93694"
  }

def insert_data(page):
  querystring = {"id":"4149559506737816","page":str(page)}
  try:
    response = requests.request("GET", url, headers=headers, params=querystring)
    time.sleep(3)
  except:
    pass

  # print(response.text)

  # response.encoding = response.apparent_encoding
  if json.loads(response.text)['ok'] == 1:
    for dt in json.loads(response.text)['data']:
      # print(dt)
      comments.insert_one(dt)

if __name__ == '__main__':
  # method1
  for i in range(60):
    insert_data(i)
  # # method2
  # pool = Pool()
  # pages = range(100000)
  # pool.map(insert_data, pages)
  # pool.close()
  # pool.join()

