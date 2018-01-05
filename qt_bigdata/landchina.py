# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm
@time:2017/7/19 10:23
"""
import bs4
from bs4 import BeautifulSoup
import re,os
import requests
import glob
import pandas as pd 

session = requests.Session()

def output_info(page):
  lst = []

  url = "http://www.landchina.com/default.aspx"
  querystring = {"tabid":"347","ComName":"default"}
  payload = {'__VIEWSTATE':'/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhwFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBYoBQ09MT1I6IzAwMDAwMDtCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X3pkcXlnZHFrXzAxLmdpZik7HwMFAjQ2FgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAQ9kFgJmD2QWAmYPZBYCZg9kFgICAQ9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAw9kFgICAw8WBB4JaW5uZXJodG1sBYMHPHAgYWxpZ249ImNlbnRlciI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZTogeC1zbWFsbCI+Jm5ic3A7PGJyIC8+DQombmJzcDs8YSB0YXJnZXQ9Il9zZWxmIiBocmVmPSJodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vIj48aW1nIGJvcmRlcj0iMCIgYWx0PSIiIHdpZHRoPSIyNjAiIGhlaWdodD0iNjEiIHNyYz0iL1VzZXIvZGVmYXVsdC9VcGxvYWQvZmNrL2ltYWdlL3Rkc2N3X2xvZ2UucG5nIiAvPjwvYT4mbmJzcDs8YnIgLz4NCiZuYnNwOzxzcGFuIHN0eWxlPSJjb2xvcjogI2ZmZmZmZiI+Q29weXJpZ2h0IDIwMDgtMjAxNCBEUkNuZXQuIEFsbCBSaWdodHMgUmVzZXJ2ZWQmbmJzcDsmbmJzcDsmbmJzcDsgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KdmFyIF9iZGhtUHJvdG9jb2wgPSAoKCJodHRwczoiID09IGRvY3VtZW50LmxvY2F0aW9uLnByb3RvY29sKSA/ICIgaHR0cHM6Ly8iIDogIiBodHRwOi8vIik7DQpkb2N1bWVudC53cml0ZSh1bmVzY2FwZSgiJTNDc2NyaXB0IHNyYz0nIiArIF9iZGhtUHJvdG9jb2wgKyAiaG0uYmFpZHUuY29tL2guanMlM0Y4Mzg1Mzg1OWM3MjQ3YzViMDNiNTI3ODk0NjIyZDNmYScgdHlwZT0ndGV4dC9qYXZhc2NyaXB0JyUzRSUzQy9zY3JpcHQlM0UiKSk7DQo8L3NjcmlwdD4mbmJzcDs8YnIgLz4NCueJiOadg+aJgOaciSZuYnNwOyDkuK3lm73lnJ/lnLDluILlnLrnvZEmbmJzcDsmbmJzcDvmioDmnK/mlK/mjIE65rWZ5rGf6Ie75ZaE56eR5oqA6IKh5Lu95pyJ6ZmQ5YWs5Y+4Jm5ic3A75LqR5Zyw572RPGJyIC8+DQrlpIfmoYjlj7c6IOS6rElDUOWkhzA5MDc0OTky5Y+3IOS6rOWFrOe9keWuieWkhzExMDEwMjAwMDY2NigyKSZuYnNwOzxiciAvPg0KPC9zcGFuPiZuYnNwOyZuYnNwOyZuYnNwOzxiciAvPg0KJm5ic3A7PC9zcGFuPjwvcD4fAQVkQkFDS0dST1VORC1JTUFHRTp1cmwoaHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL1VzZXIvZGVmYXVsdC9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjdzIwMTNfeXdfMS5qcGcpO2RkYbZ40T1d+JmzzzD8H2fRDxDj6CwinAzx3sYOrZDC8js=',
    '__EVENTVALIDATION':'/wEWAgKgpJ7QBwLN3cj/BPlscKZFAh35ltst3eUh+/eZs02kYaUpTePr9l+0Bo/7',
    'hidComName':'default',
    'TAB_QuerySubmitPagerData':page}
  headers = {
    'x-devtools-request-id': "3060.466",
    'origin': "http://www.landchina.com",
    'x-devtools-emulate-network-conditions-client-id': "55f36b5a-6c53-4846-9295-bf9b60ab427c",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://www.landchina.com/default.aspx?tabid=347&ComName=default",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "ASP.NET_SessionId=na5inwp0iuy2ennzlym4tpcv; Hm_lvt_83853859c7247c5b03b527894622d3fa=1500363664,1500430121; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1500430507; Hm_lvt_83853859c7247c5b03b527894622d3fa=1500363664,1500430121; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1500430730",
    'cache-control': "no-cache",
    'postman-token': "80ff43ef-7378-d75a-d144-08c8c8f39d22"
    }

  # response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
  response = session.post(url,data=payload, headers=headers, params=querystring)
  response.encoding = response.apparent_encoding
  # print(response.text)
  soup = BeautifulSoup(response.text,'lxml').select('#TAB_contentTable > tbody')[0]
  info = soup('a',target="_blank")
  for tag in info:
    if isinstance(tag,bs4.element.Tag):
      url = 'http://www.landchina.com/' + tag['href']
      # print(url)
      lst.append(url)

  return lst

def get_txt(path,url):
  headers = {
      # 'upgrade-insecure-requests': "1",
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
      'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
      'accept-encoding': "gzip, deflate",
      'accept-language': "zh-CN,zh;q=0.8",
      'cookie': "ASP.NET_SessionId=iobrcpxuehov520dfdffb2op; Hm_lvt_83853859c7247c5b03b527894622d3fa=1500430121,1500440754,1500516539,1500529091; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1500529346",
      'cache-control': "no-cache",
      # 'postman-token': "6b2227dd-57d9-377d-aabd-9a3d94c39e09"
      }
  r = requests.request("GET", url, headers=headers)
  r.encoding = r.apparent_encoding
  soup = BeautifulSoup(r.text,'lxml')
  trs = soup.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1 > tbody')[0]('tr')[2:]
  with open(path,'w+',encoding='utf-8') as f:
    for tr in trs:
      row = []
      for td in tr('td'):
        word = td.text.strip()
        row.append(word)
      f.write(','.join(row)+'\n')

def main1():
  # 下载导航页链接
  path = 'C:/Users/qt_52/Desktop/landchina/'
  if not os.path.exists(path):os.mkdir(path)
  for page in range(1,50):
    page_lst = output_info(page)
    with open(path+str(page)+'.txt','w',encoding='utf-8') as f:
      for url in page_lst:
        f.write(url+'\n')

def main2():
  links = []
  for txt in glob.glob(nav_path):
    # print(txt)
    with open(txt,'r',encoding='utf-8') as f:
      for line in f.readlines():
        links.append(line.strip())
  for i,link in enumerate(links):
    name = link.split('=')[-1]
    txt_path = save_path + name + '.txt'
    if os.path.exists(txt_path):
      print('\rcur_link already exists!',end='')
      continue
    print('cur_name is:',name,i+1,len(links))
    get_txt(txt_path,link)
    
def main3(path):
  all_info = []
  for txt in glob.glob(path):
    one_page = []
    with open(txt,'r',encoding='utf-8') as f:
      for line in f.readlines():
        one_page.extend(line.strip().split(','))
    all_info.append(one_page)
  pd.DataFrame(all_info).to_csv(root_dir+'landchina.csv',index=False,encoding='utf-8')



if __name__ == '__main__':
  root_dir = 'D:/myData/qt_spider_data/landchina/'
  nav_path = root_dir + 'navig/*.txt'
  save_path = root_dir + 'txt_info/'
  # main1()
  # main2()
  main3(save_path+'*.txt')