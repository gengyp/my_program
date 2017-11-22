# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm
@time:2017/11/22 10:28
"""
import requests
import random
import time
def get_proxies():
  # 公司自购代理IP调用接口
  params = {'num': '200', 'type': '1', 'pro': '', 'city': '0', 'yys': '0', 'port': '11', 'time': '1',
            'ts': '0', 'ys': '0', 'cs': '0', 'lb': '1', 'sb': '0', 'pb': '4', 'mr': '1', 'regions': ''}
  response = requests.get('http://webapi.http.zhimacangku.com/getip', params=params).text.strip().split('\r\n')
  return response


def save2sql(lst):
  # 检查表中是否存在数据
  import pymysql
  conn = pymysql.connect(host='localhost',user='root',passwd='root',db='scraping',charset='utf8')
  cursor = conn.cursor()
  
  del_sql = 'delete from yw_proxy'
  insert_sql = 'insert into yw_proxy values("{}")'
  cursor.execute(del_sql)
  for ip in lst:
    print(ip)
    cursor.execute(insert_sql.format(ip))
  conn.commit()

  cursor.close()
  conn.close()

def select_sql():
  # 检查表中是否存在数据
  import pymysql
  conn = pymysql.connect(host='localhost', user='root', passwd='root', db='scraping', charset='utf8')
  cursor = conn.cursor()

  sql = 'select *  from yw_proxy'
  cursor.execute(sql)
  values = cursor.fetchall()
  print(values)
  ip = random.choice(values)
  print(ip[0])
  
  # conn.commit()

  cursor.close()
  conn.close()
  
  
if __name__ == '__main__':
  while True:
    ips = get_proxies()
    # print(ips)
    save2sql(ips)
    time.sleep(5*60)
    