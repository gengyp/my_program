# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@author GengYanpeng
@software:PyCharm
@time:2017/7/20 9:42

"""
from __future__ import print_function
import requests
import bs4
import time
from bs4 import BeautifulSoup
import pymysql
import random


class yiwFlight(object):
  """docstring for ClassName"""
  
  def __init__(self):
    self.session = requests.Session()
    self.headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=aff228d3-dcbb-407b-9602-f1b066176bba; traceExt=campaign=CHNbaidu81&adid=index; HotelCityID=36split%E5%A4%A7%E7%90%86%E5%B8%82splitDalisplit2017-11-9split2017-11-10split0; FD_SearchHistorty={"type":"S","data":"S%24%u676D%u5DDE%28HGH%29%24HGH%242017-11-15%24%u6606%u660E%28KMG%29%24KMG"}; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1510208762729%7D%5D; adscityen=Hangzhou; DomesticUserHostCity=HGH|%ba%bc%d6%dd; ASP.NET_SessionSvc=MTAuMTUuMTI4LjMxfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTUwOTk3MTQxNTQ1Nw; FlightIntl=Search=%5B%22HANGZHOU%7C%E6%9D%AD%E5%B7%9E(HGH)%7C17%7CHGH%7C480%22%5D; StartCity_Pkg=PkgStartCity=17; _bfa=1.1510208628240.o5yke.1.1510208628240.1511140628961.2.41; _bfs=1.35; page_time=1511140872045%2C1511140875582%2C1511140890442%2C1511140898522%2C1511140950341%2C1511140981657%2C1511140982959%2C1511140983451%2C1511140996342%2C1511141005408%2C1511141011584%2C1511141061057%2C1511141119920%2C1511141176440%2C1511141186056%2C1511141191945%2C1511141195771%2C1511141198021%2C1511141200366%2C1511141246096%2C1511141283717%2C1511141286830%2C1511141303404%2C1511141313855%2C1511141337591; _RF1=122.225.202.162; _RSG=0oaEYCqpLR3YZKkUbICUE9; _RDG=2859957a96d6ff26a503e2d19e475e86c5; _RGUID=36d5cf43-223a-4c80-939e-31295eb948e2; _ga=GA1.2.560308012.1510208631; _gid=GA1.2.1346787746.1511140649; __zpspc=9.2.1511140648.1511141340.30%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1511140648585%7C1.848442986.1510208631115.1511141316568.1511141340276.1511141316568.1511141340276.undefined.0.0.35.35; MKT_Pagesource=PC; appFloatCnt=25; _bfi=p1%3D151001%26p2%3D151001%26v1%3D41%26v2%3D40',
                    'Host': 'flights.ctrip.com',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    self.conn = pymysql.connect(host='192.168.36.80', user='root', passwd='Temp@1026', db='apiDB', charset='utf8')
    self.cursor = self.conn.cursor()
    self.conn1 = pymysql.connect(host='192.168.36.80', user='root', passwd='Temp@1026', db='gyp_test', charset='utf8')
    self.cursor1 = self.conn1.cursor()
    self.proxies = self.get_proxies()

  def soup2lst(self, html):
    # 解析网页逐条存入数据库
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.select('#tab1 > table > tbody')[0]('tr')
    for tr in trs:
      row = [time.strftime('%Y-%m-%d', time.localtime(time.time()))]
      # row = [time.strftime('%Y-%m-%d', time.localtime(time.time() - 1.8 * 3600))]
      if isinstance(tr, bs4.element.Tag):
        for td in tr('td')[:-1]:
          # row.append(td.text.strip())
          row.append(td.text.strip().replace(' ', ''))
      # print(row)
      # save2sql(row)
      self.save2sql_new(row)
  
  def save2sql(self, lst):
    # 检查表中是否存在数据
    sql = 'select * from ctripfligtinfo where date="{}" and flightNo="{}"'.format(lst[0], lst[1])
    exists_item = self.cursor.execute(sql)
    
    # 删除已存在的数据
    if exists_item != 0:
      del_sql = 'delete from ctripfligtinfo where date="{}" and flightNo="{}"'.format(lst[0], lst[1])
      self.cursor.execute(del_sql)
    
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
    self.cursor.execute(sql.format(lst[0], lst[1], lst[2], lst[3], s[0], s[1], s[2], s[3], s[4], s[5], lst[-1]))
    self.conn.commit()
  
  def save2sql_new(self, lst):
    # 检查表中是否存在数据
    sql = 'select * from ctripfligtinfo where date="{}" and flightNo="{}"'.format(lst[0], lst[1])
    exists_item = self.cursor.execute(sql)
    
    # 数据变换
    s = []  # 六个时刻信息
    for t in lst[4:7]:
      if t == '':
        s.extend(['', ''])
      elif '\n\n' in t:
        s.extend(t.split('\n\n'))
      else:
        s.extend([t, ''])
    
    # 存在则更新，不存在插入的数据
    if exists_item != 0:
      sql = 'update ctripfligtinfo set leaveAirport="{}", arriveAirport="{}", forcastTakeoffTime="{}",forcastLandingTime="{}",realTakeoffTime="{}",realLandingTime="{}", status="{}" where date="{}" and flightNo="{}"'
      self.cursor.execute(sql.format(lst[2], lst[3],s[2], s[3], s[4], s[5], lst[-1], lst[0], lst[1]))
    else:
      # 插入数据
      sql = 'insert into ctripfligtinfo values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'
      self.cursor.execute(sql.format(lst[0], lst[1], lst[2], lst[3], s[0], s[1], s[2], s[3], s[4], s[5], lst[-1]))
    self.conn.commit()
  
  def get_proxies(self):
    # 生成随机 ip_port
    # conn1 = pymysql.connect(host='192.168.36.80',user='root',passwd='Temp@1026',db='gyp_test',charset='utf8')
    # cursor1 = conn1.cursor()
    # cursor1.execute('select ip_port from yw_proxy')
    # values = cursor.fetchall()
    # # proxy_ip = random.choice(values)
    # cursor1.close()
    # conn1.close()
    # return values
    
    self.cursor1.execute('select ip_port from yw_proxy')
    values = self.cursor1.fetchall()
    # proxy_ip = random.choice(values)
    return values

  def save2ip(self, ip):
    # 检查表中是否存在数据
    import pymysql
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='scraping',charset='utf8')
    cursor = conn.cursor()
    
    sql = 'insert into available_ywproxy values("{}")'.format(ip)
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

  def spiderHtml(self, name):
    url = "http://flights.ctrip.com/actualtime/" + name + '.p'
    flag = True
    count = 0
    while flag:
      try:
        ip_port = random.choice(self.proxies)[0]
        proxies = {"http": "http://" + ip_port}
        # print(proxies)
        if count >= 50:
          proxies = None
        response = requests.get(url + '1/', headers=self.headers, proxies=proxies,timeout=2)
        # response = requests.get(url + '1/', headers=self.headers)
        print('\ncur name:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), name, response.status_code,
              response.url)
        self.soup2lst(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        page_num = int(soup.select('#tab1 > div.clearfix > div > div.c_page_list.layoutfix > a')[-1].text)
        for i in range(2, page_num + 1):
          new_url = url + str(i) + '/'
          response = requests.get(new_url, headers=self.headers, proxies=proxies,timeout=2)
          # response = requests.get(new_url, headers=self.headers)
          self.soup2lst(response.text)
        flag = False
        # self.save2ip(ip_port) 
      except Exception as e:
        # print(ip_port)
        self.cursor1.execute('delete from yw_proxy where ip_port="{}"'.format(ip_port))
        self.conn1.commit()
        count += 1
        print('\rip request failed !!!!', count, end='')
        pass
  
  def testProxyIp(self, iplist):
    url = 'http://flights.ctrip.com/actualtime'
    for j, ipPort in enumerate(iplist):
      for i in range(5):
        try:
          r = requests.get(url, proxies={'http': 'http://' + ipPort})
          if r.status_code != 200:
            print('\rtest faild')
            break
        except Exception as e:
          print('requests error', e)
          break
      print(j, ipPort)

  def closedb(self):
    self.cursor.close()
    self.conn.close()
    self.cursor1.close()
    self.conn1.close()


if __name__ == '__main__':
  yw = yiwFlight()
  names = ['arrive-yiw', 'depart-yiw']
  start = time.time()
  flag1 = True
  try:
    while flag1:
      for name in names:
        yw.spiderHtml(name)
      cur_hour = time.localtime().tm_hour
      if cur_hour >= 2 and cur_hour < 6:
          time.sleep(5 * 60 * 60 + 10 * 60)
      else:
        time.sleep(2 * 60)
      if time.time() - start > 12 * 60:
        # flag1 = False
        break
  except Exception as e:
    print('异常关闭!', e)
  finally:
    yw.closedb()
