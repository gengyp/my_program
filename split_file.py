# coding:utf-8

'''
seg dir file to n part
'''
from __future__ import print_function
import shutil
import os,glob

raw_path = '/Users/gengyanpeng/Downloads/hollow_captcha'
# file_qz = os.path.basename(raw_path)

def split_num(n):
  # mkdir n dir
  for i in range(n):
     file_name = raw_path+'_'+str(i+1)
     os.mkdir(file_name)

  for i,pic_path in enumerate(glob.glob(raw_path+'/*.*')):
    pic_name = os.path.basename(pic_path)
    for j in range(n):
      if i%n==j:
         # print(pic_path,os.path.join(raw_path+'_'+str(j+1),pic_name))
         shutil.copy(pic_path,os.path.join(raw_path+'_'+str(j+1),pic_name))
    print('\rjindu:',i,end='')
  print('\n')

split_num(4)