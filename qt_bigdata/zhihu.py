# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

@author GengYanpeng
@software:PyCharm
@time:2017/7/25 16:20
"""

import os
import requests
from bs4 import BeautifulSoup
import shutil
import os
import time
import pandas as pd
import sys

work_path = 'D:/微云同步盘/871927963/Python/chinese_seg/share_program'
os.chdir(work_path)
sys.path.insert(0,work_path)
from process import Process
numclass = 12       # 文本分类数
r_ratio = 0.02      # 实词截取比例
v_ratio = numclass  # 虚词截取比例, == numclass,不保留虚词
idf_rotio = 0.95    # 根据 idf 保留词的比例

s = Process(numclass,r_ratio,v_ratio,idf_rotio)

def get_data(path):
  info = []
  with open(path,'r',encoding='utf-8') as f:
    html = f.read()
  soup = BeautifulSoup(html,'lxml')
  divs = soup.select('#QuestionAnswers-answers > div > div > div:nth-of-type(2)')[0]('div')
  print(len(divs))
  for i,div in enumerate(divs):
    # print(div.select('div.ContentItem-meta > div > div.AuthorInfo > div > div.AuthorInfo-detail > div > div')[0].text,i)
    print(i)
    # 'div.ContentItem-meta > div > div.AuthorInfo > div > div.AuthorInfo-detail > div > div'
    for span in div('span'):
      print(span.text)
      # info.append(p.text.strip().replace(' ',''))
  # print(len(info),len(set(info)))
  # print(info)
  return info

if __name__ == '__main__':
  from collections import Counter
  html_path = 'C:/Users/qt_52/Desktop/zhihu/zhihu.html'
  txt_path = 'C:/Users/qt_52/Desktop/zhihu/zhihu_pinglu.txt'
  data = get_data(html_path)
  # s.save2txt(set(data),'12.txt')
  # print(set(data))
  # s.load_dict()
  # new_data = []
  # for i,line in enumerate(data):
  #   titleL = s.ProcessChar(line)
  #   new_data.append(titleL)
  # # print(new_data,len(list(set(new_data))))

  # temp = [] 
  # wdfreq = Counter(s.data2text(new_data))  # 统计词频
  # # print(wdfreq)





  # allword = list(wdfreq)
  # # print(allword)
  # wdpos = s.getwordpos(allword)
  # print('\n词向量长度:',len(allword),';去停词后:-',len(wdpos),'=',len(allword)-len(wdpos))
  # realwd,virwd = s.vir_wd(wdpos)
  # print('real word num:',len(realwd),'vir word num:',len(virwd))
  # print(realwd)
  # for k in realwd:
  #   temp.append([k,wdfreq[k]])
  # print(os.getcwd())
  # pd.DataFrame(temp).to_csv('123.csv',index=False,encoding='utf-8')



  # # with open(txt_path,'w',encoding='utf-8') as f:
  # #   for line in data:
  # #     f.write(''.join(line)+'\n')
  # # print('over!')
