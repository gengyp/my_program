# -*- coding:utf-8 -*-
import requests
import bs4,re,os
import pandas as pd
import json

from bs4 import BeautifulSoup

def getHtmlText(url):
  try:
    r = requests.get(url,timeout=30)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print('requests fail!')
    return None

def getlinks(html):
  lst = []
  soup = BeautifulSoup(html,'html.parser')
  for tag in soup('a',style="float: left;"):
    lst.append(tag['href'])
  return lst

def getinfolinks(links):
  lst = []
  for link in links:
    html = getHtmlText(link)
    soup = BeautifulSoup(html,'html.parser')
    tag = soup.find('ul',{'class':'menuul'})
    if tag is None:
      tag = soup.find('ul',{'class':'nav_con'})
    url = 'http://yichen.b2b.jctrans.com' + tag.findAll('a')[1]['href']
    print(url)
    lst.append(url)
  return lst


def infooutput(errorlst,urls):
  infolst = []
  errorlst = []
  for i,url in enumerate(urls):
    row = []
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'html.parser')
    if 'about' in url:
      title = soup.h1.string.strip()
      reobj = re.search(r'.[jpg|png|JPG|PNG]\" />\s*</div>\s*(.*?)\s*<div',html,flags=re.S)
      if reobj is None:
        errorlst.append(url)
        context = None
        print('正则不匹配:',url)
      else:
        context = reobj.group(1)
    elif 'Info' in url:
      tag = soup.find('div',{'class':'contxt'})
      title = tag.h1.string.strip()
      context = tag.p.text.strip()
    elif 'OrdinaryMember' in url:
      tag = soup.find('div',{'class':'contxt'})
      title = tag.h1.string.strip()
      context = tag.p.text.strip()
    else:
      errorlst.append(url)
      print(url)
      title=None
      context = None

    row.append(title)
    row.append(context)

    try:
      tableinfo = soup.find('table')
      tds = tableinfo('td')
      for td in tds:
        row.append(td.string.strip())
    except:
      pass
    row.append(url)
    infolst.append(row)
    print('\rtotal links is: {}\t the current is: {}'.format(len(urls),i+1),end = '')

  df = pd.DataFrame(infolst)
  return df



if __name__ == '__main__':
  startpage = 1
  try:
    df = pd.DataFrame()
    errlst = []
    for i in range(startpage,1700):
      print('The current page is :%d'% i )
      url = 'http://company.jctrans.com/Company/List/2140-0----0/'+str(i)+'.html'
      html = getHtmlText(url)
      if html is None:
        print('导航页错误……',url)
      links = getlinks(html)
      nlinks = getinfolinks(links)
      ndf = infooutput(errlst,nlinks)
      if ndf is None:
        continue
      if i == startpage:
        col = ['comname','intro','zhuc','zhucnum','zhucaddr','zhuccode','addr',
        'code','faren','capital','type','period','range','deji','check','url']
        df = ndf.copy()
        df.columns = col
      else:
        df = df.append(ndf) # 追加，原 df 保持不变
      print('\r当前进度：%.2f%%' % (100*(i+1)/1700),end='')
    print(errlst)
  except:
    pass
  finally:
    df.index = range(df.shape[0])
    df.to_excel('customs_broker.xls')
