# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

@author GengYanpeng
@software:PyCharm
@time:2017/8/9 10:34
从凤凰网（社会、历史、文化、房产、科技、体育、财经、教育、娱乐）
腾讯新闻（社会、历史、文化、房产、科技、体育、财经、教育、娱乐）
一个用于训练，一个用于测试；path = 'D:/myData/china_seg'
具体爬取方式：
思路1：按类别爬取，txt格式，名为日期+编号。txt 1st line 为title
思路2：全站爬取，保存 csv（title,content,url),根据 url 解析类别,以下采用 思路2
keyword = ['society','history','culture','house','tech','sports','finance','edu','ent','cul']
"""
import os
import requests
from bs4 import BeautifulSoup 
import pymysql
import numpy as np
import bs4

keyword = ['society','history','culture','house','tech','sports','finance','edu','ent','cul']
headers = {
  # 'upgrade-insecure-requests': "1",
  'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
  'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  'accept-encoding': "gzip, deflate",
  'accept-language': "zh-CN,zh;q=0.8",
  # 'cache-control': "no-cache",
  }

def get_ip():
  conn = pymysql.connect(host='127.0.0.1',user='root',password='root',db='scraping',charset='utf8')
  cursor = conn.cursor()
  ip_list = []
  try:
    cursor.execute('SELECT content FROM valid_ip where test_times>7')
    result = cursor.fetchall()
    for i in result:
      ip_list.append(i[0])
  except Exception as e:
    print (e)
  finally:
    cursor.close()
    conn.close()
  return ip_list

proxies = get_ip()
print(proxies[:5])
proxy = {'http','http://'+np.random.choice(proxies)}

def getHtml(link):
  while True:
    try:
      proxy = {'http':'http://'+np.random.choice(proxies)}
      r = requests.get(link,headers =headers ,proxies=proxy)
      if r.status_code != 200:
        print('\r',r.status_code,end='')
        continue  
      else:
        r.encoding = r.apparent_encoding
        return r.text
    except:
      # continue
      r = requests.get(link,headers =headers)
      r.encoding = r.apparent_encoding
      print('local ip response status:',r.status_code)
      return  r.text  

def get_text_info(url):
  try:
    name = '_'.join(url.split('.')[-2].split('/')[-2:])+'.txt'
    if os.path.exists(name):
      return
  except:
    print('url not split:',url)
  try:
    soup = BeautifulSoup(getHtml(url),'lxml')
    # soup = get_soup(url)
    title = soup.select('#artical_topic')[0].text
    # title = soup.select('body > div.yc_main.wrap > div.yc_tit > h1')[0].text
    # '#artical_topic'body > div.yc_main.wrap > div.yc_tit > h1
    content = []
    ps = soup.select('#main_content')[0]('p')
    # ps = soup.select('body > div.yc_main.wrap > div.yc_con.clearfix > div.yc_con_l')[0]('p')
    # '#main_content'body > div.yc_main.wrap > div.yc_con.clearfix > div.yc_con_l
  except:
    print('parser url error:',url)
    return
  for p in ps:
    content.append(p.text)
    # print(p.text)
  with open(name,'w+',encoding='utf8') as f:
    f.write(url+'\n')
    f.write(title+'\n')
    f.write(' '.join(content))

def get_text_links(link):
  # 获取凤凰文本链接
  soup = BeautifulSoup(getHtml(link),'lxml')
  # soup = get_soup(link)
  # lis = soup.select('body > div.main > div.left > div')[0]('li')
  # lis = soup.select('body > div.yc_main.clearfix > div.yc_m_l > div > div')[0]('div')
  # lis = soup.select('body > div.main.back > div.mainLeft > div.mainLM > div.comListCon')[0]('div')
  lis = soup.select('body > div.col.clearfix > div.col_L > div.box650')[0]('div')
  # lis = soup.select('#box_content')[0]('div')
  # #box_content

  for li in lis:
    if isinstance(li,bs4.element.Tag):
      try:
        link = li.a['href']
        v = get_text_info(link)
        if v is None:
          print('\ralready exists!',end='')
      except:
        pass
  # return soup.select('body > div.main > div.left > div > div.nextPage > div.m_page > span:nth-of-type(2) > a')[0]['href']
  return soup.select('#pagenext')[0]['href']
  # #pagenext

if __name__ == '__main__':
  keyword = ['society','history','culture','house','tech','sports','finance','edu','ent','cul']
  path = 'D:/myData/china_seg/text_ifeng/%s'%keyword[5]
  if not os.path.exists(path):os.mkdir(path)
  os.chdir(path)

  url = 'http://tech.ifeng.com/listpage/801/14/list.shtml?cflag=1&prevCursorId=44630587&cursorId=44629837'  # 文本链接导航页

  url = 'http://sports.ifeng.com/listpage/31194/6/1/51518444/51532011/list.shtml'
  url = 'http://sports.ifeng.com/listpage/11247/4/1/51593028/51600612/list.shtml'

  for i in range(30):
    print('\npage is:',i+1,url)
    url = get_text_links(url)

  # 但文本链接
  # url = 'http://news.ifeng.com/a/20170810/51605419_0.shtml'




