# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/7/14 17:30
"""
import requests
import json,os
from urllib.request import quote
import time

def spider_id(career,city):
  for pn in range(1,31):
    lst = spider_id_one(career,city,pn)
  return lst

def spider_id_one(career,city,pn):
  lst = []
  url = "https://www.lagou.com/jobs/positionAjax.json"

  querystring = {"px":"default","city":city,"needAddtionalResult":"false"}

  payload = {'first':'false', 'pn':pn, 'kd':career}
  headers = {
      'origin': "https://www.lagou.com",
      'x-anit-forge-code': "0",
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
      'content-type': "application/x-www-form-urlencoded",
      'accept': "application/json, text/javascript, */*; q=0.01",
      'x-requested-with': "XMLHttpRequest",
      'x-anit-forge-token': "None",
      'referer': "https://www.lagou.com/jobs/list_{}?px=default&city={}".format(quote(career),quote(city)),
      'accept-encoding': "gzip, deflate, br",
      'accept-language': "zh-CN,zh;q=0.8",
      'cookie': "user_trace_token=20170424161403-e5a0c7d072b54c46a84805fb39b6dea4; LGUID=20170424161404-fad738b4-28c5-11e7-b333-525400f775ce; JSESSIONID=ABAAABAACDBABJB8451B1BD68375031EC01BE799FA745AC; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; _gat=1; _gid=GA1.2.1056728853.1500425742; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500022216,1500425741; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500428040; _ga=GA1.2.740843107.1493021642; LGSID=20170719085547-00a4dcb1-6c1d-11e7-a349-525400f775ce; LGRID=20170719093406-5aa43862-6c22-11e7-ab1d-5254005c3644; SEARCH_ID=a9da39512c4e43dca812cc3301f3d9ed",
      'cache-control': "no-cache",
      'postman-token': "00c32c58-40f0-f580-e6a7-aa0a96dd71c9"
      }
  response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
  # print(response.text)
  try:
    r = json.loads(response.text)
    for key in r['content']['hrInfoMap'].keys():
      lst.append(key)
  except:
    with open(failed_path,'a+',encoding='utf-8') as f:
      temp = [career,city,str(pn)]
      f.write(' '.join(temp)+'\n')
    print(response.url)
  return lst

def main1():
  cities = ['安庆','澳门特别行政区','鞍山','安阳','阿勒泰','安康','北京','保定','包头','宝鸡','北海','滨州','蚌埠','毕节','百色','本溪','巴彦淖尔','成都','长沙','重庆','常州','沧州','承德','郴州','潮州','赤峰','常德','昌吉','滁州','朝阳','楚雄','东莞','大连','东营','德阳','大同','大理','大庆','德州','达州','丹东','迪庆','恩施','鄂尔多斯','佛山','福州','阜阳','抚州','阜新','防城港','抚顺','广州','贵阳','桂林','赣州','广元','甘孜藏族自治州','广安','高雄','贵港','杭州','合肥','哈尔滨','海口','惠州','呼和浩特','湖州','邯郸','淮安','黄石','河源','菏泽','衡阳','衡水','河池','鹤壁','淮南','淮北','葫芦岛','汉中','黄冈','黄山','呼伦贝尔','和田','海西','贺州','怀化','鹤岗','济南','嘉兴','金华','江门','济宁','荆州','吉林','揭阳','晋中','九江','景德镇','焦作','锦州','吉安','晋城','嘉峪关','酒泉','荆门','佳木斯','昆明','开封','克拉玛依','兰州','廊坊','临沂','洛阳','柳州','连云港','拉萨','丽水','泸州','聊城','临汾','六盘水','六安','乐山','凉山彝族自治州','娄底','辽阳','丽江','漯河','龙岩','辽源','绵阳','梅州','茂名','马鞍山','眉山','牡丹江','南京','宁波','南昌','南宁','南通','南阳','南充','宁德','内江','南平','濮阳','莆田','攀枝花','平顶山','盘锦','萍乡','青岛','泉州','秦皇岛','清远','黔东南','黔西南','衢州','黔南','齐齐哈尔','曲靖','日照','上海','深圳','苏州','石家庄','沈阳','绍兴','汕头','三亚','韶关','十堰','邵阳','商丘','上饶','宿迁','宿州','遂宁','松原','商洛','汕尾','随州','石嘴山','三沙','三门峡','三明','四平','朔州','天津','太原','台州','唐山','泰州','泰安','台中','铜仁','通化','台北','铁岭','武汉','无锡','温州','乌鲁木齐','潍坊','芜湖','威海','梧州','吴忠','武威','渭南','西安','厦门','徐州','西宁','咸阳','香港特别行政区','新乡','邢台','襄阳','湘潭','信阳','西双版纳','咸宁','许昌','孝感','湘西土家族苗族自治州','新余','宣城','新北','烟台','扬州','银川','盐城','宜昌','阳泉','玉溪','运城','阳江','益阳','延边','宜宾','岳阳','营口','云浮','延安','雅安','玉林','永州','伊犁','鹰潭','郑州','珠海','中山','长春','淄博','湛江','肇庆','镇江','株洲','漳州','长治','遵义','张家口','舟山','资阳','周口','驻马店','枣庄','中卫']
  careers = ['java','ui','产品经理','运营','市场','销售','hr','行政','财务','风控','python','总监','设计师']
  careers = ['数据']
  for career in careers:
    print('career is:',career)
    if os.path.exists(save_path+career+'.txt'):continue
    with open(save_path+career+'.txt','w+',encoding='utf-8') as f:
      for city in cities:
        id_lst = spider_id(career,city)
        print('city is:',city,len(id_lst))
        for cid in id_lst:
          f.write(cid+'\n')

def main2(path):
  with open(path,'r',encoding='utf-8') as f:
    for line in f.readlines():
      s = line.strip().split(' ')
      id_lst = spider_id_one(s[0],s[1],int(s[2]))
      print('city is:',s[0],s[1],len(id_lst))
      print(id_lst)

if __name__ == '__main__':
  save_path = 'D:/myData/qt_spider_data/lagou/'
  failed_path = save_path + 'failed.txt'
  if not os.path.exists(save_path):os.mkdir(save_path)
  main1()
  # main2(failed_path)


