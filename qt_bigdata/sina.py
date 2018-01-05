# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

@author GengYanpeng
@software:PyCharm
@time:2017/7/28 13:33
"""

import bs4
from bs4 import BeautifulSoup
import re,os
import requests
import glob
import pandas as pd 

url = "http://culture.ifeng.com/listpage/59666/2/1/51423046/list.shtml"

headers = {
  # 'x-devtools-request-id': "8636.34945",
  'x-devtools-emulate-network-conditions-client-id': "5ce58b48-3a92-4267-9418-c58955c15433",
  'upgrade-insecure-requests': "1",
  'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
  'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  # 'referer': "http://tech.sina.com.cn/notebook/",
  'accept-encoding': "gzip, deflate",
  'accept-language': "zh-CN,zh;q=0.8",
  'cookie': "U_TRS1=000000a2.55d95242.58eb24a8.d159f346; UOR=www.baidu.com,blog.sina.com.cn,; SINAGLOBAL=122.225.202.162_1491805353.448726; vjuids=650674638.15b56876b16.0.022c6d490da43; SGUID=1494829922550_82415079; SCF=Ap2RvUnIOa3aBfS8dbOi-r4HH-FlQzvE2CDjgu-TmGwFMLQddqixBtKuPdPO47OAPQnvljy-DsEZfT_Vel04R3Y.; SUB=_2AkMucvuXf8NxqwJRmPwcyW7hboR-zQDEieKYLgpMJRMyHRl-yD83qhQStRCtElISwoyKm7rierNbzMbq1TzisQ..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWsnijvxKomnYoXB6lZ65O5; bdshare_firstime=1501202567323; Apache=122.225.202.162_1501204255.699861; ULV=1501204408240:15:4:4:122.225.202.162_1501204255.699861:1501204254146; U_TRS2=000000a2.6dc04adc.597a8fbb.2a0e4953; hqEtagMode=1; vjlast=1501220154; SSCSum=2; lxlrttp=1500433109",
  'cache-control': "no-cache",
  # 'postman-token': "a5a8b904-6ed5-0dc4-6df1-0e3954609a82"
    }
def get_links(lst,html):
  soup = BeautifulSoup(html,'lxml')
  # divs = soup.select('body > div.col.clearfix > div.col_L > div.box650')[0]('div')
  divs = soup.select('#feedCardContent > div:nth-of-type(1)')[0]('div')
  # '#feedCardContent > div:nth-child(1) > div:nth-child(31)'
  # '#feedCardContent > div:nth-child(1) > div:nth-child(1) > h2 > a'
  print('text num:',len(divs))
  for div in divs:
    try:
      lst.append(div.select('h2 > a')[0]['href'])
      # lst.append(div.select('h3 > a')[0]['href'])
    except:
      # print(div.select('h2 > a'))
      continue
  try:
    divs = soup.select('#feedCardContent > div:nth-of-type(1) > div:nth-of-type(31)')[0]('div')
    # '#feedCardContent > div:nth-child(1) > div:nth-child(31)'
    # '#feedCardContent > div:nth-child(1) > div:nth-child(1) > h2 > a'
    print('text num:',len(divs))
    for div in divs:
      try:
        lst.append(div.select('h2 > a')[0]['href'])
        # lst.append(div.select('h3 > a')[0]['href'])
      except:
        # print(div.select('h2 > a'))
        continue

    divs = soup.select('#feedCardContent > div:nth-of-type(1) > div:nth-of-type(32)')[0]('div')
    # '#feedCardContent > div:nth-child(1) > div:nth-child(31)'
    # '#feedCardContent > div:nth-child(1) > div:nth-child(1) > h2 > a'
    print('text num:',len(divs))
    for div in divs:
      try:
        lst.append(div.select('h2 > a')[0]['href'])
        # lst.append(div.select('h3 > a')[0]['href'])
      except:
        # print(div.select('h2 > a'))
        continue
  except:
    pass

def opentxt(savepath):
  # 读取 savepath.txt 中的元素，返回 list
  lst = []
  with open(savepath,'r',encoding='utf-8') as f:
    for line in f.readlines():
      lst.append(line.strip())
  return lst

def save2txt(lst,savepath):
  # 将 lst 中每个元素按行保存在 txt 中
  with open(savepath,'w+',encoding='utf-8') as f:
    for wd in lst:
      try:
        f.write(''.join(wd) + '\n')
      except:
        print('write error:',wd)

if __name__ == '__main__':
  path = 'D:/myData/china_seg/fudan_corpus/rawdata/else_test/C19-Computer/'

  # links = []
  # for i in range(3):
  #   link_path = 'C:/Users/qt_52/Desktop/sina/page%s.html'%(i+1)
  #   with open(link_path,'r',encoding='utf-8') as f:
  #     html = f.read()
  #   get_links(links,html)

  # save2txt(links,path+'links.txt')

  links = opentxt(path+'links.txt')
  print(len(links))

  for i,link in enumerate(links):
    # link = 'http://culture.ifeng.com/a/20170727/51513980_0.shtml'
    txt_num = link.strip('.shtml').split('/')[-1]
    
    if txt_num in ''.join(os.listdir(path)):
      print('存在！')
      continue

    r = requests.get(link,headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'lxml')
    try:
      filepath = path + txt_num + soup.select('#main_title')[0].text.strip()+'.txt'  
      filepath = re.sub(r'[|"|”|“|：|?|？]','',filepath)
      content = ''
      ps = soup.select('#artibody')[0]('p')
      for p in ps:
        content += p.text.strip()
      with open(filepath,'w+',encoding='utf-8') as f:
        f.write(content)
      print('\r当前进度：',(i+1),len(links),end='')
    except:
      pass