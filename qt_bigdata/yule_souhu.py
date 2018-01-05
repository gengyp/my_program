# -*- coding:utf-8 -*-
"""
爬取 搜狐娱乐信息
"""
import requests

url = "http://yule.sohu.com/_scroll_newslist/20170918/news.inc"

headers = {
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    'accept': "text/javascript, application/javascript, */*",
    'cache-control': "no-cache",
    'x-devtools-emulate-network-conditions-client-id': "245d1a46-8b02-4cd4-871d-615d62e5e1dd",
    'x-requested-with': "XMLHttpRequest",
    'if-modified-since': "Thu, 01 Jan 1970 00:00:00 GMT",
    'expires': "-1",
    'referer': "http://yule.sohu.com/roll/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "vjuids=-7373f5f53.15a1345ac3d.0.fc2196ab816d4; sci12=w:1; sohutag=8HsmeSc5NCwmcyc5NjwmYjc5NSwmYSc5NCwmZjc5NCwmZyc5NCwmbjc5NCwmaSc5NCwmdyc5NCwmaCc5NCwmYyc5NCwmZSc5NCwmbSc5NCwmdCc5NH0; beans_mz_userid=HgrRd0HxIJo5; debug_test=sohu_third_cookie; IPLOC=CN3301; SUV=1701131022097321; vjlast=1489662282.1505719257.21",
    'postman-token': "3c335b09-fbfa-7791-f522-caffa3419af0"
    }

response = requests.request("GET", url, headers=headers)
response.encoding = response.apparent_encoding

print(response.text)

category = re.findall(r'\[\".*?\"\]',response.text)
item = re.findall(r'\[\d{1,2}.*?\"\]',response.text)


