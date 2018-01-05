# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/9/18 16:38
http://ent.qq.com/articleList/rolls/
目标：爬取腾讯娱乐与明星相关文章 并入库
字段信息有：title url newstime c_type

涉及知识点：
mysql 数据库的插入
时间格式的转换

"""
from __future__ import print_function
# import requests
import json,re
import pymysql
import time,datetime

url = "http://roll.news.qq.com/interface/cpcroll.php"

headers = {'Accept':'*/*',
 'Accept-Encoding':'gzip, deflate',
 'Accept-Language':'zh-CN,zh;q=0.8',
 'Cache-Control':'no-cache',
 'Connection':'keep-alive',
 'Cookie':'vjuids=-7373f5f53.15a1345ac3d.0.fc2196ab816d4; sci12=w:1; sohutag=8HsmeSc5NCwmcyc5NjwmYjc5NSwmYSc5NCwmZjc5NCwmZyc5NCwmbjc5NCwmaSc5NCwmdyc5NCwmaCc5NCwmYyc5NCwmZSc5NCwmbSc5NCwmdCc5NH0; beans_mz_userid=HgrRd0HxIJo5; debug_test=sohu_third_cookie; IPLOC=CN3301; SUV=1701131022097321; vjlast=1489662282.1505719257.21; mobileUV=1_15996aa61c3_31842; tvfe_boss_uuid=11199f1eaf43f00e; RK=AC36bVbOUD; pac_uid=1_871927963; pgv_pvi=805214208; pgv_si=s6998268928; idt=1503445629; rv2=80E5FF5AE7B91885186C304A431AA82E1C308C2C21025DA27B; property20=5F41040A2E42DE0A127C2F7C2DCE9BD60B03BAB61D689A47CB34C5A2D89F0AE422D31DB3511C367B; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; ptisp=ctc; ptcz=5456ec48846db8eefa7dced70b2e8b0a0baa3f36d12df05d9c4b611af0bf3880; pt2gguin=o0871927963; uin=o0871927963; skey=@QIrv6XaZ7; pgv_info=ssid=s7347757538; pgv_pvid=3300736656; o_cookie=871927963',
 'Host':'roll.news.qq.com',
 'Pragma':'no-cache',
 'Referer':'http://ent.qq.com/articleList/rolls/',
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


connect = pymysql.Connection(host='192.168.36.38',user='root',passwd='123456',db='xingtiao',charset='utf8')
cursor = connect.cursor()

table_name = 'star_content'

# querystring = {'callback':'rollback',
#  'site':'ent',
#  'mode':'1',
#  'cata':'',
#  'date':'2017-09-18',
#  'page':'1',
#  '_':'1505721655587'}

def one_page(url,querystring):
  # 爬取一个连接所有信息并入库
  try:
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.ecoding = response.apparent_encoding
    info_dt = json.loads(re.search(r'rollback\((.*?)\)',response.text).group(1))['data']
  except:
    with open('mx_error.txt','a+',encoding='utf-8') as f:
      print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+ response.request.url +" 插入失败",file=f)
    return
  try:
    page_num = info_dt['count']
  except:
    print('cur url')
    page_num = 1
  for dt in info_dt['article_info']:
    # print(dt)
    title = dt['title']
    url = dt['url']
    newstime = dt['time']
    c_type = dt['column']
    s = [title,url,newstime,c_type]
    try:
      item_exist = cursor.execute('SELECT * FROM %s WHERE url="%s"' %(table_name, url))
      # 新增代理数据入库
      if item_exist == 0:
        # 插入数据
        # cursor.execute('INSERT INTO %s VALUES("%s","%s", '', "%s", "%s")'%(table_name,s[0],s[1],s[2],s[3]))
        n = cursor.execute('INSERT INTO %s VALUES(null,"%s","%s", "", "%s", "%s")'%(table_name,s[0],s[1],s[2],s[3]))
        connect.commit()
        # 输出入库状态
        if n:
          print ('\r',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+ url +" 插入成功",end='')
        else:
          with open('mx_error.txt','a+',encoding='utf-8') as f:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+ response.request.url +" 插入失败",file=f)
      else:
        print ('\r',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+ url  +" 已存在",end='')
    except Exception as e:
      print ("入库失败：" + str(e))
  return page_num

def get_info2db(start,end):
  # 获取指定日期的所有链接
  datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
  dateend=datetime.datetime.strptime(end,'%Y-%m-%d')
  rand = 1505736957027
  while datestart <= dateend:
    flag = True
    page_num = 1
    str_date = datestart.strftime('%Y-%m-%d')
    print('\ncur spider date:',str_date)

    while flag:
      querystring = {'callback':'rollback',
       'site':'ent',
       'mode':'1',
       'cata':'',
       'date':str_date,
       'page':str(page_num),
       '_':str(rand)}

      max_num = one_page(url,querystring)
      if max_num == None:
        break
      time.sleep(1)
      rand += 2
      if page_num < max_num:
        page_num += 1
      else:
        flag = False
    datestart += datetime.timedelta(days=1)

def main():
  start = '2017-09-5'
  end = '2017-09-18'

  get_info2db(start,end)

  cursor.close()
  connect.close()


if __name__ == '__main__':
  main()









