# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm
@time:2017/11/22 10:28

手法
1. 考虑到要更换 ip 池：主程序每12分钟后终止一次，更新一次ip池
2. 航班过零点，考虑到每条更新完整度，让写入数据库时间比实际小 1.8h ，0.2h 写入当天数据
3. 在凌晨2-6之间代码不工作
4. 代理ip 请求失败超过50次时，用本机请求
5. 每隔一段时间新增一批代理ip，并将请求失败的代理ip删除
6. 考虑代码的迁移性，数据库打开后正常关闭
"""
import requests
import random
import time
import os

def get_proxies():
  # 公司自购代理IP调用接口
  # params = {'num': '200', 'type': '1', 'pro': '', 'city': '0', 'yys': '0', 'port': '11', 'time': '1',
  #           'ts': '0', 'ys': '0', 'cs': '0', 'lb': '1', 'sb': '0', 'pb': '4', 'mr': '1', 'regions': ''}
  # response = requests.get('http://webapi.http.zhimacangku.com/getip', params=params)

  response = requests.get('http://webapi.http.zhimacangku.com/getip?num=200&type=1&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
  # print(response.url,response.text)
  return response.text.strip().split('\r\n')

def add2sql(lst):
  import pymysql
  conn = pymysql.connect(host='192.168.36.80',user='root',passwd='Temp@1026',db='gyp_test',charset='utf8')
  # conn = pymysql.connect(host='localhost',user='root',passwd='root',db='scraping',charset='utf8')
  cursor = conn.cursor()
  insert_sql = 'insert into yw_proxy values(null,"{}")'
  for ip in lst:
    try:
       cursor.execute(insert_sql.format(ip))
    except Exception as e:
      print('insert ip to db error!', e)
  conn.commit()

  cursor.close()
  conn.close()

def select_sql():
  # 检查表中是否存在数据
  import pymysql
  conn = pymysql.connect(host='localhost', user='root', passwd='root', db='scraping', charset='utf8')
  cursor = conn.cursor()

  sql = 'select ip_port  from yw_proxy'
  cursor.execute(sql)
  values = cursor.fetchall()
  print(values)
  ip = random.choice(values)
  print(ip[0])
  
  # conn.commit()

  cursor.close()
  conn.close()
  
  
if __name__ == '__main__':
  count = 0
  while True:
    count += 1
    ips = get_proxies()
    # print(ips)
    add2sql(ips)
    print('\r第{}轮ip更新中...'.format(count),end='\n')
    os.system('python yiwFlight.py')
    print('第{}轮ip更新结束'.format(count))
    time.sleep(60)
