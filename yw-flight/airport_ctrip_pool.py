# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@author GengYanpeng
@software:PyCharm
@time:2017/7/20 9:42

并行版本

"""
import numpy as np
import requests
import bs4, os
import pandas as pd
import time
from multiprocessing import Pool
from bs4 import BeautifulSoup

session = requests.Session()
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding':'gzip, deflate',
 'Accept-Language':'zh-CN,zh;q=0.9',
 'Cache-Control':'max-age=0',
 'Connection':'keep-alive',
 'Cookie':'Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=aff228d3-dcbb-407b-9602-f1b066176bba; traceExt=campaign=CHNbaidu81&adid=index; HotelCityID=36split%E5%A4%A7%E7%90%86%E5%B8%82splitDalisplit2017-11-9split2017-11-10split0; FD_SearchHistorty={"type":"S","data":"S%24%u676D%u5DDE%28HGH%29%24HGH%242017-11-15%24%u6606%u660E%28KMG%29%24KMG"}; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1510208762729%7D%5D; adscityen=Hangzhou; DomesticUserHostCity=HGH|%ba%bc%d6%dd; ASP.NET_SessionSvc=MTAuMTUuMTI4LjMxfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTUwOTk3MTQxNTQ1Nw; FlightIntl=Search=%5B%22HANGZHOU%7C%E6%9D%AD%E5%B7%9E(HGH)%7C17%7CHGH%7C480%22%5D; StartCity_Pkg=PkgStartCity=17; _bfa=1.1510208628240.o5yke.1.1510208628240.1511140628961.2.41; _bfs=1.35; page_time=1511140872045%2C1511140875582%2C1511140890442%2C1511140898522%2C1511140950341%2C1511140981657%2C1511140982959%2C1511140983451%2C1511140996342%2C1511141005408%2C1511141011584%2C1511141061057%2C1511141119920%2C1511141176440%2C1511141186056%2C1511141191945%2C1511141195771%2C1511141198021%2C1511141200366%2C1511141246096%2C1511141283717%2C1511141286830%2C1511141303404%2C1511141313855%2C1511141337591; _RF1=122.225.202.162; _RSG=0oaEYCqpLR3YZKkUbICUE9; _RDG=2859957a96d6ff26a503e2d19e475e86c5; _RGUID=36d5cf43-223a-4c80-939e-31295eb948e2; _ga=GA1.2.560308012.1510208631; _gid=GA1.2.1346787746.1511140649; __zpspc=9.2.1511140648.1511141340.30%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1511140648585%7C1.848442986.1510208631115.1511141316568.1511141340276.1511141316568.1511141340276.undefined.0.0.35.35; MKT_Pagesource=PC; appFloatCnt=25; _bfi=p1%3D151001%26p2%3D151001%26v1%3D41%26v2%3D40',
 'Host':'flights.ctrip.com',
 'Upgrade-Insecure-Requests':'1',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

def opentxt(path):
  lst = []
  with open(path, 'r') as f:
    for line in f.readlines():
      lst.append(line.strip())
  return lst

def proxies():
  params = {'num':'200','type':'1','pro':'','city':'0','yys':'0','port':'11','time':'1',
  'ts':'0','ys':'0','cs':'0','lb':'1','sb':'0','pb':'4','mr':'1','regions':''}
  ips = session.get('http://webapi.http.zhimacangku.com/getip',params=params).text.strip().split('\r\n')
  return ips


save_path = './update_data1/'
if not os.path.exists(save_path): os.mkdir(save_path)
names = opentxt('./airport.txt')
proxy_ips = proxies()

def soup2lst(html,info_lst):
  soup = BeautifulSoup(html, 'lxml')
  trs = soup.select('#tab1 > table > tbody')[0]('tr')
  for tr in trs:
    row = []
    if isinstance(tr, bs4.element.Tag):
      for td in tr('td'):
        row.append(td.text.strip().replace(' ', ''))
      info_lst.append(row)

def randomProxy():
  proxy_ip = np.random.choice(proxy_ips)
  proxies = {'http': "http://" + proxy_ip}
  # print(proxies)
  return proxies

def spiderHtml(name):
  info_lst = []
  xlsx_path = save_path + name + '.xlsx'
  # if os.path.exists(xlsx_path):continue
  url = "http://flights.ctrip.com/actualtime/airport-" + name + '.p'
  Flag = True
  while Flag:
    try:
      ip_port = randomProxy()
      response = session.get(url + '1', headers=headers, proxies=ip_port)
      if response.status_code == 200:
        Flag = False
      soup2lst(response.text,info_lst)
      soup = BeautifulSoup(response.text, 'lxml')
      page_num = int(soup.select('#tab1 > div.clearfix > div > div.c_page_list.layoutfix > a')[-1].text)
      chi_name = soup.select('#main > div.location > a:nth-of-type(3)')[0].text
      print('cur city name:',chi_name,name,response.url)

      for i in range(2, page_num + 1):
        new_url = url + str(i)
        response = session.get(new_url, headers=headers, proxies=ip_port)
        # time.sleep(np.random.choice(1,3))
        soup2lst(response.text,info_lst)
    except:
      print('cur city faild !!!!',name)
      pass
    # print(info_lst)
  col_name = ['航班号', '出发机场', '到达机场', '计划起降时间', '预估起降时间', '实际起降时间', '状态', '操作']
  pd.DataFrame(info_lst, columns=col_name).to_excel(xlsx_path, index=False, encoding='utf-8')


if __name__ == '__main__':
  pool = Pool(processes=4)
  pool.map(spiderHtml, names)
  pool.close()
  pool.join()
