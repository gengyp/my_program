# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/7/14 9:24
"""

import requests
import re,os,shutil
from bs4 import BeautifulSoup

def getHtmlText(url):
  try:
    r = requests.get(url,timeout=30)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print('requests fail!')
    return

def get_date(v):
  """获取有道翻译翻译结果"""
  url = 'http://shuju.wdzj.com/plat-info-initialize.html'
  # 创建数据字典
  payload = {'wdzjPlatId':str(v)}
  response = requests.post(url, data=payload)                # 请求表单数据
  return response.text



def main(path):
  url = 'http://shuju.wdzj.com/'
  html = getHtmlText(url)
  soup = BeautifulSoup(html,'lxml')
  infos = soup.select('#platTable > tr > td.td-item.td-platname > div > a')

  p2p_num = {}
  for info in infos:
    try:
      num = re.search(r'-(\d+)?\.html',info['href']).group(1)
      name = info.text.strip()
    except:
      pass
    if name not in p2p_num:
      p2p_num[name] = num

  cunzai = list(map(lambda x: re.search(r'_(.*)?\.txt',x).group(1),os.listdir(path)))

  count = 0
  for k,v in p2p_num.items():
    count += 1
    if k in cunzai:
      continue
    try:
      data = get_date(v)
    except:
      continue
    with open(path+str(v)+'_'+k+'.txt','w',encoding='utf-8') as f:
      f.write(data)
    print('download:',count,514)


if __name__ == '__main__':
  data_save_path = '/Users/gengyanpeng/Desktop/p2p_data/'
  if os.path.exists(data_save_path):shutil.rmtree(data_save_path)
  os.mkdir(data_save_path)
  main(data_save_path)
