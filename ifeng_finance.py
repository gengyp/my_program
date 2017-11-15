# -*- coding: utf-8 -*-

'''
/html/body/div[8]/div/div[2]/div/table/tbody/tr[2]/td[1]/a
//tbody//a[@target="_blank"]
http://app.finance.ifeng.com/list/stock.php?t=ha&f=symbol&o=asc&p=1     id
http://app.finance.ifeng.com/data/stock/tab_gsjj.php?symbol=    公司简介
http://app.finance.ifeng.com/data/stock/tab_cwjk.php?symbol=600000&day=2016-12-31&go=next   财务简介

name  /html/body/div[9]/div[2]/div[2]/table/tbody/tr[1]/td[2]/text()
mishu  /html/body/div[9]/div[2]/div[2]/table/tbody/tr[5]/td[2]/text()
add     /html/body/div[9]/div[2]/div[2]/table/tbody/tr[6]/td[2]/text()
phone  /html/body/div[9]/div[2]/div[2]/table/tbody/tr[7]/td[2]/text()

营业收入  /html/body/div[9]/div[2]/table/tbody/tr[4]/td[3]/text()
净利润     /html/body/div[9]/div[2]/table/tbody/tr[50]/td[3]/text()
'''
import random
import re
import requests
import time
from lxml import etree



# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class spider:
  '''
  
    '''
  
  def __init__(self):
    self.urls_id = ['http://app.finance.ifeng.com/list/stock.php?t=ha&f=symbol&o=asc&p=' + str(i) for i in range(26, 28)]
    self.gsjj_api = 'http://app.finance.ifeng.com/data/stock/tab_gsjj.php?symbol='
    self.cwjk_api = 'http://app.finance.ifeng.com/data/stock/tab_cwjk.php?symbol=' + '&day=2016-12-31&go=next'
    self.ids = []
    import pymysql
    self.conn = pymysql.connect(host='192.168.36.80',user='root',passwd='Temp@1026',db='gyp_test',charset='utf8')
    # self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='scraping', charset='utf8')
    self.cursor = self.conn.cursor()
  
  def getPage(self):
    for url in self.urls_id:
        r = requests.get(url)
        tree = etree.HTML(r.text)
        idlist = tree.xpath('//td[position()=1]/a[@target="_blank"]/text()')
        # idlist = re.findall('http://finance\.ifeng\.com/app/hq/stock/sh(\d+)/index\.shtml', r.text)
        self.ids += idlist
    
    # ids = ['600000']
    for s_id in self.ids:
      u = 'http://app.finance.ifeng.com/data/stock/tab_gsjj.php?symbol=' + str(s_id)
      # print(u)
      r = requests.get(u)
      r.encoding = r.apparent_encoding
      
      tree = etree.HTML(r.text)
      try:
        name = tree.xpath('//tr[1]/td[2]/text()')
      except:
        name = ['']
      try:
        mishu = tree.xpath('//tr[5]/td[2]/text()')
      except:
        mishu = ['']
      try:
        add = tree.xpath('//tr[6]/td[2]/text()')
      except:
        add = ['']
      try:
        phone = tree.xpath('//tr[7]/td[2]/text()')
      except:
        phone = ['']
      a = 'http://app.finance.ifeng.com/data/stock/tab_lrb.php?symbol=' + str(s_id) + '&day=2017-03-31&go=next'
      r = requests.get(a)
      r.encoding = r.apparent_encoding
      t = etree.HTML(r.text)
      try:
        yysr = t.xpath('//tr[4]/td[3]/text()')
      except:
        yysr = ['']
      try:
        jly = t.xpath('//tr[50]/td[3]/text()')
      except:
        jly = ['']

      s = [s_id,name[0],mishu[0],add[0],phone[0],''.join(yysr[0].split(' ')), ''.join(jly[0].split(' '))]
      self.save2db(s)
      print(s)
      # time.sleep(random.randint(1, 3))
  
  def save2db(self, s):
    # sql = 'insert into stock_info values("600008","北京首创股份有限公司","邵丽","北京市朝阳区北三环东路八号静安中心三层","--010-64689035","7912040562","610888930")'
    sql = 'insert into stock_info values("{}","{}","{}","{}","{}","{}","{}")'.format(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
    self.cursor.execute(sql)
    self.conn.commit()
    
  def close_w(self):
    self.cursor.close()
    self.conn.close()

if __name__ == '__main__':
  obj = spider()
  obj.getPage()
  # obj.save2db()
  obj.close_w()



