# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@author GengYanpeng
@software:PyCharm
@time:2017/7/20 9:42

六个时刻点插入本地数据库用于分析网站不同时刻数据差异
'00:10', '1:10', '7:10', '12:10', '20:10', '23:10'
结论：当天航班会追踪到凌晨前一分钟，第二天六个小时航班数有递增（39，69，72）
且过了零点，前一天数据消失
"""
import requests
import bs4
import time
from bs4 import BeautifulSoup
import pymysql
# import random

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': 'Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=aff228d3-dcbb-407b-9602-f1b066176bba; traceExt=campaign=CHNbaidu81&adid=index; HotelCityID=36split%E5%A4%A7%E7%90%86%E5%B8%82splitDalisplit2017-11-9split2017-11-10split0; FD_SearchHistorty={"type":"S","data":"S%24%u676D%u5DDE%28HGH%29%24HGH%242017-11-15%24%u6606%u660E%28KMG%29%24KMG"}; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1510208762729%7D%5D; adscityen=Hangzhou; DomesticUserHostCity=HGH|%ba%bc%d6%dd; ASP.NET_SessionSvc=MTAuMTUuMTI4LjMxfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTUwOTk3MTQxNTQ1Nw; FlightIntl=Search=%5B%22HANGZHOU%7C%E6%9D%AD%E5%B7%9E(HGH)%7C17%7CHGH%7C480%22%5D; StartCity_Pkg=PkgStartCity=17; _bfa=1.1510208628240.o5yke.1.1510208628240.1511140628961.2.41; _bfs=1.35; page_time=1511140872045%2C1511140875582%2C1511140890442%2C1511140898522%2C1511140950341%2C1511140981657%2C1511140982959%2C1511140983451%2C1511140996342%2C1511141005408%2C1511141011584%2C1511141061057%2C1511141119920%2C1511141176440%2C1511141186056%2C1511141191945%2C1511141195771%2C1511141198021%2C1511141200366%2C1511141246096%2C1511141283717%2C1511141286830%2C1511141303404%2C1511141313855%2C1511141337591; _RF1=122.225.202.162; _RSG=0oaEYCqpLR3YZKkUbICUE9; _RDG=2859957a96d6ff26a503e2d19e475e86c5; _RGUID=36d5cf43-223a-4c80-939e-31295eb948e2; _ga=GA1.2.560308012.1510208631; _gid=GA1.2.1346787746.1511140649; __zpspc=9.2.1511140648.1511141340.30%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1511140648585%7C1.848442986.1510208631115.1511141316568.1511141340276.1511141316568.1511141340276.undefined.0.0.35.35; MKT_Pagesource=PC; appFloatCnt=25; _bfi=p1%3D151001%26p2%3D151001%26v1%3D41%26v2%3D40',
           'Host': 'flights.ctrip.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

# conn = pymysql.connect(host='192.168.36.80', user='root', passwd='Temp@1026', db='apiDB', charset='utf8')


def soup2lst(html):
  # 解析网页逐条存入数据库
  soup = BeautifulSoup(html, 'lxml')
  trs = soup.select('#tab1 > table > tbody')[0]('tr')
  for tr in trs:
    row = [time.strftime('%Y-%m-%d', time.localtime())]
    if isinstance(tr, bs4.element.Tag):
      for td in tr('td')[:-1]:
        # row.append(td.text.strip())
        row.append(td.text.strip().replace(' ', ''))
    # print(row)
    save2sql(row)
    # save2sql_new(row)

def save2sql(lst):
  conn = pymysql.connect(host='localhost', user='root', passwd='root', db='scraping', charset='utf8')
  cursor = conn.cursor()
  # # 检查表中是否存在数据
  # sql = 'select * from ctripfligtinfo where date="{}" and flightNo="{}"'.format(lst[0], lst[1])
  # exists_item = cursor.execute(sql)
  #
  # # 删除已存在的数据
  # if exists_item != 0:
  #   del_sql = 'delete from ctripfligtinfo where date="{}" and flightNo="{}"'.format(lst[0], lst[1])
  #   cursor.execute(del_sql)
  
  # 数据变换
  s = []
  for t in lst[4:7]:
    if t == '':
      s.extend(['', ''])
    elif '\n\n' in t:
      s.extend(t.split('\n\n'))
    else:
      s.extend([t, ''])
  # 插入数据
  sql = 'insert into ctripfligtinfo values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'
  cursor.execute(sql.format(lst[0], lst[1], lst[2], lst[3], s[0], s[1], s[2], s[3], s[4], s[5], lst[-1]))
  conn.commit()
  cursor.close()
  conn.close()

def spiderHtml(name):
  url = "http://flights.ctrip.com/actualtime/" + name + '.p'
  Flag = True
  while Flag:
    try:
      # response = requests.get(url + '1/', headers=headers, proxies=ip_port)
      response = requests.get(url + '1/', headers=headers)
      print('cur name:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), name, response.status_code, response.url)
      soup2lst(response.text)
      soup = BeautifulSoup(response.text, 'lxml')
      page_num = int(soup.select('#tab1 > div.clearfix > div > div.c_page_list.layoutfix > a')[-1].text)
      for i in range(2, page_num + 1):
        new_url = url + str(i) + '/'
        # response = requests.get(new_url, headers=headers, proxies=ip_port)
        response = requests.get(new_url, headers=headers)
        soup2lst(response.text)
      Flag = False
    except:
      print('ip request faild !!!!')
      return


def testProxyIp(iplist):
  url = 'http://flights.ctrip.com/actualtime'
  for j, ipPort in enumerate(iplist):
    for i in range(5):
      try:
        r = requests.get(url, proxies={'http': 'http://' + ipPort})
        if r.status_code != 200:
          print('\rtest failed')
          break
      except:
        print('requests error')
        break
    print(j, ipPort)


if __name__ == '__main__':
  names = ['arrive-yiw', 'depart-yiw']
  # save_hour = ['00:10', '1:10', '7:10', '12:10', '20:10', '23:10']
  save_hour = [0, 23]
  while True:
    if time.localtime(time.time() - 10 * 60).tm_hour in save_hour:
      for name in names:
        spiderHtml(name)
    time.sleep(1 * 3600)
