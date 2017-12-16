# -*- coding:utf-8 -*-
import requests
import bs4,re,os
import pandas as pd 
import json

from bs4 import BeautifulSoup

def getHtmlText(url):
  try:
    r = requests.get(url)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print('requests fail!')
    return None

def getcity(lst,html):
  # <ul id="allprovince">
  soup = BeautifulSoup(html,'html.parser')
  info = soup.find('ul',id="allprovince")
  infos = info('a',href="###")
  for tag in infos:
    lst.append(tag.string)

def infoprint(html):
  regexp = re.compile(r'\[\[.*?\]\]')
  rg = regexp.search(html)
  if rg is None:
    return None
  else:
    lst = json.loads(rg.group(0))
    for info in lst:
      info[-1] = info[-1].strip()
      # print(info)
    col = ['year','prov','citycode','city','countycode','county','EAI','WI','aEDI','Xrank','Prank']
    df = pd.DataFrame(lst)
    df.columns = col 
    return df 


start_url = 'http://www.aliresearch.com/html/stopic/aedi/'
citylst = []
html = getHtmlText(start_url)
getcity(citylst,html)
df = pd.DataFrame()
for i,prov in enumerate(citylst):
  url = 'http://www.aliresearch.com/api/aedi/static.php?ctype=aedi&\
  prov='+str(prov)+'&callback=jQuery17101615287811222279_1494323236290&_=1494323236403'
  # print(url)
  html = getHtmlText(url)
  ndf = infoprint(html)
  if i == 1:  
    df = ndf.copy()
  else:
    df = df.append(ndf) # 追加，原 df 保持不变
  print('\r当前进度：%.2f%%' % (100*(i+1)/len(citylst)),end='')

df.index = range(df.shape[0])
df.to_excel('aEDI.xls')



