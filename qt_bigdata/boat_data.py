# -*- coding:utf-8 -*-
import requests
import bs4,re,os
import pandas as pd 
import shutil

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

def infoprint(html):
  lst = []
  soup = BeautifulSoup(html,'html.parser')
  for tr in soup.find('table').children:
    if isinstance(tr,bs4.element.Tag):
      row = []
      tds = tr('td')
      for td in tds:
        row.append(td.text.strip())
      # print(row)
      lst.append(row)
  if len(lst)<=1:
    return None
  else:
    lst = lst[1:]
    col = ['name','line','num','people']
    df = pd.DataFrame(lst)
    df.columns = col 
    return df 

if __name__ == '__main__':
  mypath = r'C:\\Users\\qt_52\\Desktop\\123'
  if os.path.exists(mypath):
    shutil.rmtree(mypath)
    os.mkdir(mypath)
  else:
    os.mkdir(mypath)
  os.chdir(mypath)

  df = pd.DataFrame()
  for i in range(1,9):
    url = 'http://chuanqi.jctrans.com/searoutes/chuanqi/'+str(i)+'.html'
    # print(url)
    html = getHtmlText(url)
    ndf = infoprint(html)
    if i == 1:  
      df = ndf.copy()
    else:
      df = df.append(ndf) # 追加，原 df 保持不变
    print('\r当前进度：%.2f%%' % (100*i/8),end='')

  df.index = range(df.shape[0])
  df.to_excel('boat.xls')



