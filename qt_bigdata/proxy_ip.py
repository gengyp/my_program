# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

@author GengYanpeng
@software:PyCharm
@time:2017/7/21 15:16
"""

import re
import time
import requests

session = requests.Session()


def get_kuaidaili_ip(url="http://www.kuaidaili.com/free/outha/1"):
  headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://www.kuaidaili.com/free/outha/1",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "yd_cookie=56328545-6317-480ae33a864c8d7d1c9a43734ea15b4498db; _ydclearance=0baeaa78192662e327491e99-4df3-40cd-84b2-5ff0b31ebb57-1500607852; channelid=0; sid=1500600187128626; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1500600650; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1500600650; _ga=GA1.2.682061729.1500600650; _gid=GA1.2.2088126049.1500600650",
    'cache-control': "no-cache",
  }
  r = session.get(url, headers=headers)
  r.encoding = r.apparent_encoding
  return r.text


def get_xicidaili_ip(url="http://www.xicidaili.com/nn"):
  headers = {

  }
  r = session.get(url, headers=headers)
  r.encoding = r.apparent_encoding
  return r.text


def get_data5u_ip(url="http://www.data5u.com/"):
  headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://www.kuaidaili.com/free/outha/1",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "yd_cookie=56328545-6317-480ae33a864c8d7d1c9a43734ea15b4498db; _ydclearance=0baeaa78192662e327491e99-4df3-40cd-84b2-5ff0b31ebb57-1500607852; channelid=0; sid=1500600187128626; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1500600650; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1500600650; _ga=GA1.2.682061729.1500600650; _gid=GA1.2.2088126049.1500600650",
    'cache-control': "no-cache",
    # 'postman-token': "cc1a37da-978a-3a81-3653-755e7ae72b9e"
  }
  r = session.get(url, headers=headers)
  r.encoding = r.apparent_encoding
  return r.text


def getProxyList(url, iPage=10):
  ipList = []
  for i in range(1, iPage + 1):
    html_str = get_kuaidaili_ip(url + str(i))
    ip = re.findall("IP\">((?:\d{1,3}\.){3}(?:\d{1,3}))(?:[\s\S]{0,50})\"PORT\">(\d{2,4})", html_str)
    for addr in ip:
      ipList.append(addr[0] + ":" + addr[1])
    time.sleep(2)
  return ipList


def validate_ip(ip_port):
  try:
    r = requests.get(validate_url, proxies={'proxy': "http://" + ip_port}, timeout=5)
    return r.status_code
  except:
    print('connect failed')
    return


if __name__ == '__main__':
  # 代理 ip 保存地址
  ip_txt_path = 'C:/Users/qt_52/Desktop/airport_ctrip/proxy.txt'
  # 待验证网址
  validate_url = 'http://flights.ctrip.com/actualtime/airport-xiaoshan/'
  # 代理ip 网址
  url = "http://www.kuaidaili.com/free/outha/"

  ipList = getProxyList(url, 5)  # 爬取1页

  valid_ip = []

  for i,ip in enumerate(ipList):
    v = validate_ip(ip)
    if v == 200:
      print(i+1,v)
      valid_ip.append(ip)
  with open(ip_txt_path, 'w+', encoding='utf-8') as f:
    for ip in valid_ip:
      f.write(ip + '\n')
