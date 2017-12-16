# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm
@time:2017/9/9 16:56
目标：爬取北京 58 同城二手市场所有商品信息(商家和个人)
数据库：bj58_2shou（nav_link,goods_info）
step1 获取所有导航页链接信息到数据库
step2 从数据库读取商品链接，并爬取商品信息入库并打印
"""

import requests
import bs4, os
import pandas as pd
import time

from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
bjershou = client['bj58_2shou']
nav_link = bjershou['nav_link']
goods_info = bjershou['goods_info']

# host_url = 'http://hz.58.com'
host_url = 'http://bj.58.com'
state_url = host_url + '/sale.shtml'

def getHtmlText(url):
  try:
    r = requests.get(url)
    time.sleep(2)
    print('cur url state:', url, r.status_code)
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print('requests fail!')
    return


def channel_extract(state_url):
  links = []
  html = getHtmlText(state_url)
  soup = BeautifulSoup(html, 'lxml')
  for tag in soup.select('li.ym-tab > span.dlb > a'):
    try:
      links.append(host_url + tag['href'])
    except:
      pass
  return links

def get_nav_links(link,type=0,page=1):
  # http://bj.58.com/shouji/0/pn2/
  all_link = []
  for dt in nav_link.find():
    all_link.append(dt['url'])
    # print(dt['url'])
  while True:
    url = link + str(type) + '/' + 'pn' + str(page) + '/'
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'lxml')
    if soup.find('td',{'class':'t t_b'}):
      for tag in soup.select('tbody > tr > td.t > a'):
        try:
          if tag['href'] not in all_link:
            data = {'url':tag['href']}
            nav_link.insert_one(data)
            print(data)
          else:
            continue
        except:
          print('解析错误',tag)
    else:
      break
    page += 1

def get_goods_info(link):
  html = getHtmlText(link)
  soup = BeautifulSoup(html,'lxml')
  title = soup.select('div > h1')
  time = soup.select('li.time')
  count = soup.select('li.count > em')
  price = soup.select('div.su_con > span[class="price c_f50"]')
  area = list(soup.select('span[class="c_25d"]').stripped_string
  print(title,time,count,price,area)



if __name__ == '__main__':
  # links = channel_extract(state_url)
  link = 'http://bj.58.com/shouji/'
  # get_nav_links(link)
  link = 'http://bj.58.com/shouji/31188582346159x.shtml?adtype=1&PGTID=0d300024-0000-16f8-13d5-6493ab35b115&entinfo=31188582346159_0&psid=195120989197267513437032680&iuType=_undefined&ClickID=2'
  get_goods_info(link)




