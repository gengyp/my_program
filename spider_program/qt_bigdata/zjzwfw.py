# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/7/14 9:24
爬虫注意事项：
1、由于数量较多，可以先爬取导航页，存于 id_path 以相应区间命名
2、遍历导航页,爬取所需信息，存于 info,对于已存在的txt跳过。post 失败存于 failed.txt
3、对 txt 处理：打不开的、信息多余的txt直接删除，并将 k v 写入 failed.txt
4、failed 剪切到 id_path 继续爬取，重复 2、3 直至 failed.txt 为空
5、对 info 目录进行转换成 csv 格式
注：日后可以对 k v 进行保存到 mysql or mongodb 中，可删除 info 中 txt
"""
import glob,string
import requests
from bs4 import BeautifulSoup
import re, bs4, time
import os, shutil
import numpy as np
import pymongo
import pymysql
import pandas as pd 

total_num = 401437
interval = 120
session = requests.Session()
headers = {
  'accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
  'origin': "http://xyxx.zjzwfw.gov.cn",
  'x-requested-with': "XMLHttpRequest",
  'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  'content-type': "application/x-www-form-urlencoded",
  'referer': "http://xyxx.zjzwfw.gov.cn/zjcreditzwfw/html/promptsList.jsp?id=96CFC60C35F527A811D198BC91914AA1778A71FD595B1228",
  'accept-encoding': "gzip, deflate",
  'accept-language': "zh-CN,zh;q=0.8",
  'cookie': "gs_b_tas=BZQX5HP6DY6RHY29; JSESSIONID=9F0B8F20B9D06D1B6BA6C0067B1502A8",
  'cache-control': "no-cache",
  'postman-token': "bc679906-ced2-b606-6ece-e299ba1ea229"
}

def getHtmlText(start, end):
  try:
    url = 'http://xyxx.zjzwfw.gov.cn/zjcreditzwfw/html/promptsProxy.jsp'
    payload = {'startrecord': str(start), 'endrecord': str(end), 'perpage': '20', 'totalRecord': '401437',
               'id': '96CFC60C35F527A811D198BC91914AA1778A71FD595B1228'}
    r = session.post(url, headers=headers, data=payload)  # 请求表单数据
    # r.raise_for_status
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return

def get_info(cid):
  # 根据 cid 获取信息所在网址
  try:
    url = 'http://xyxx.zjzwfw.gov.cn/zjcreditzwfw/html/promptsDetail.jsp'
    para = {'tableId': '96CFC60C35F527A811D198BC91914AA1778A71FD595B1228', 'cId': cid}
    r = session.post(url, headers=headers, data=para)
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return

def get_names(lst):
  # 将导航页信息整理成 post 可提交参数
  names = {}
  for line in lst:
    t = line.split('$')
    if t[2] not in names:
      names[t[2]] = t[1]
  return names

def get_post(cur_page):
  # 循环获取导航页信息
  start = 1 + interval * (cur_page - 1)
  for i in range(int(np.ceil(total_num / interval) - cur_page + 1)):
    """获取待爬取字典"""
    if start == int(interval*np.floor(total_num/interval)+1):
      end = total_num
    else:
      end = start + interval - 1
    html = getHtmlText(start, end)
    if html is None:
      print('此区间导航页获取失败:', start, end)
    else:
      try:
        lst = eval(re.search(r'.*(dataStore = (\[.*?,\])).*', html.strip()).group(2))
      except:
        lst = eval(re.search(r'(\["E$.*?\])', html.strip()).group(1))
        print('match error!', type(lst), len(lst))
        pass
      names = get_names(lst)
      print('\n当前页公司数:', len(names))
    start += interval
    yield names

def save_txt(string, path):
  # 将获取的信息 按行追加在文件末尾
  # 用于 failed.txt,info,导航页 信息的写入
  with open(path, 'a+', encoding='utf-8') as f:
    f.write(string)

def save_info(k, v):
  # 根据 公司名 和 cid 将公司信息保存本地指定路径
  print('当前公司:', k)
  txt_name = info_path + k + '_' + v + '.txt'
  if os.path.exists(txt_name):
    print('当前公司已存在!')
    return
  html = get_info(v)
  if html is None:
    print('post failed!', k, v)
    save_txt(k + ' ' + v + '\n', failed_path)
    return
  soup = BeautifulSoup(html, 'lxml')
  try:
    trs = soup.find('table', {'class': "table"})('tr')
    for tr in trs:
      if isinstance(tr, bs4.element.Tag):
        row = []
        tds = tr('td')
        for td in tds:
          row.append(td.text.strip())
        save_txt('|'.join(row) + '\n', txt_name)
  except:
    print('netpage parser error!', k, v)
    save_txt(k + ' ' + v + '\n', failed_path)
    return
  return 1

def id_txt2dict(path):
  # 将文本中 cname cid 转成字典
  dt = {}
  with open(path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
      line = line.replace('�|','+')
      if len(line) > 30 and ' ' in line:
        t = line.strip().split(' ')
        dt[t[0]] = t[1]
      # else:
        # print(line)

  return dt

def qt_mongo_db(dt):
  # 耗时，后期可计时，准确度量下
  # mongo database
  client = pymongo.MongoClient('localhost', 27017)
  qt_db = client['qt_spider_db']
  zjzwfw_table = qt_db['zjzwfw']
  # dt = {'cid':'85DF8BB1EF48F0F88E07E97167F37DF2','name': '高安市三旗建筑科技有限公司'}
  zjzwfw_table.update(dt,dt,upsert=True)

def insert_data2db():
  id_lst = []
  name_lst =[]
  path = 'C:/Users/qt_52/Desktop/zjzwfw/'
  for name in os.listdir(path+'info'):
    try:
      lst = name.strip('.txt').split('_')
      cid = lst[-1]
      cname = '+'.join(lst[:-1])
      data = {'cid':cid,'name':cname}
      # print(data,type(data))
      # qt_mongo_db(data)
    except:
      print(name)
      continue
    id_lst.append(cid)
    # name_lst.append(cname)
  print('实际文本个数:',len(id_lst))
  print('去重文本个数:',len(set(id_lst))) 
  # with open(path+'id_path/exist_cid.txt','w+',encoding='utf-8') as f:
  #   for name,line in zip(name_lst,id_lst):
  #     f.write(name+' '+line+'\n')

# 以下是所有数据下载完毕，处理数据的
def opentxt(path):
  # 读取 path.txt 中的元素，返回 list
  title = os.path.basename(path).strip('.txt').split('_')[-1]
  lst = [title]
  # print(lst)
  txt_info = []
  try:
    with open(path,'r',encoding='utf-8') as f:
    # with open(path,'r') as f:
      for line in f.readlines():
        # print(line)
        # if line not in txt_info:  # 去重
        txt_info.append(line.strip())
  except:
    print('delete path is:',path)
    os.remove(path)
    return
  if len(txt_info) != 4:
    print('delete path is:',path)
    os.remove(path)
  for line in txt_info:
    if '组织机构代码|法人代表' in line or '执行案由|执行时间' in line:
      continue
    else:
      lst.extend(line.strip().split('|'))
  return lst


def exists_cid(path):
  # 读取已经存在的 cname+cid 号，并返回列表。暂时用不到
  lst = []
  with open(path,'r',encoding='utf-8') as f:
    for line in f.readlines():
      lst.append(line.strip())
  return lst

# 以下为主函数
def main1():
  print('step1:爬取导航页:')
  cur_page = 1  # 如果已爬取相应页面可修改
  for i,names in enumerate(get_post(cur_page)):
    info = []
    if names is None:
      continue
    start = cur_page+i*interval
    name_id_path = root_dir + 'id_path/{}_{}.txt'.format(start,start+interval-1)
    print('爬去页面为:%d 共 3346页'%(i+cur_page))
    for k, v in names.items():
      k = re.sub(r'[%s]+'%string.punctuation,'+',k)
      info.append(k+' '+v)
    with open(name_id_path,'w+',encoding='utf-8') as f:
      for line in info:
        f.write(line+'\n')
    time.sleep(0)

def main2(path):
  for txt_path in glob.glob(path):
    print('cur file:', txt_path)
    start_t = time.time()
    names = id_txt2dict(txt_path)
    for k,v in names.items():
      temp = save_info(k, v)
      if temp is None: continue
      cur_hour = time.localtime().tm_hour
      if cur_hour < 7 or cur_hour >= 21:
        time.sleep(0)
      elif cur_hour >= 18 and cur_hour < 21:
        time.sleep(0)
      else:
        time.sleep(2)
    print('cost time:',time.time()-start_t)
    new_name = os.path.basename(txt_path)
    shutil.move(txt_path,id_path_exist+new_name)

def main3(path):
  for i,txt in enumerate(glob.glob(path+'*.txt')):
    print('\r当前进度:',i,end='')
    temp = opentxt(txt)
    if temp is None:  # 删除 txt，保存 k v
      new_name = os.path.basename(txt).strip('.txt').split('_')
      k = '+'.join(new_name[:-1])
      v = new_name[-1]
      save_txt(k + ' ' + v + '\n', failed_path)
      print(txt)
      os.remove(txt)

def main5(path):
  # 将 txt 保存为 csv
  lst=[]
  for i,txt in enumerate(glob.glob(path+'*.txt')):  # 
    # print('\r当前进度:',i,end='')
    temp = opentxt(txt)
    if temp is not None:
      lst.append(temp)
    else:
      print(txt)
      os.remove(txt)
  # col = ['cid','组织机构代码', '法人代表', '单位地址', '执行法院', '案号', '执行依据','执行案由', '执行时间', '执行金额（元）', '未执行金额（元）', '共同被执行人', '曝光日期']
  # df = pd.DataFrame(lst)
  # # df.columns =col
  # df.to_csv(zjzwfw_path,index=False,encoding='utf-8')
  return  lst


if __name__ == '__main__':
  root_dir = 'D:/myData/qt_spider_data/zjzwfw/'
  id_path = root_dir + 'id_path/*.txt'
  info_path  = root_dir + 'info/'
  id_path_exist = root_dir + 'id_path_exist/'
  failed_path = root_dir + 'failed.txt'
  # zjzwfw_path = root_dir + 'zjzwfw.csv'
  zjzwfw_path = root_dir + 'zjzwfw.txt'
  if not os.path.exists(root_dir): os.mkdir(root_dir)
  # main1()
  # main2(id_path)
  main3(info_path)
  # lst = main5(info_path)
  # with open(zjzwfw_path,'w+',encoding ='utf-8 ') as f:
  #   for line in lst:
  #     try:
  #       f.write(','.join(line)+'\n')
  #     except:
  #       print(line)

# # test one
# # k,v = ('高安市三旗建筑科技有限公司','85DF8BB1EF48F0F88E07E97167F37DF2')
# html = get_info(v)
# soup = BeautifulSoup(html,'lxml')
# trs = soup.find('table',{'class':"table"})('tr')
# trs


# for line in b:
#   a = line.split('|')
#   print(a,len(a))

# path = 'C:/Users/qt_52/Desktop/zjzwfw/info_temp/埃尔凯电器（珠海）有限公司_7F770629A068B0A948E049D20C601DA2.txt'
# with open(path,'r',encoding='utf-8') as f:
#   print(f.read())