# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/10/26 19:27
功能

test_one(pic_path,lower=60,high=161,seg=20)
参数说明：
pic_path : 待测试单张图片路径
lower，high ：二值化区间
seg ：区间间隔

test_file(pic_file,new_file=’./new_pic/’,th=127)
参数说明：
pic_file : 图片目录路径
new_file : 新图片路径，default=’./new_pic/’
th : 指定阈值

'''
from __future__ import print_function
def test_one(pic_path,lower=60,high=161,seg=20):
  import os,shutil
  from PIL import Image
  # 选取不同阈值测试图片二值化效果，保存当前文件夹 temp
  file_path = './temp/'
  if os.path.exists(file_path):
    shutil.rmtree(file_path)
  os.mkdir(file_path)

  img = Image.open(pic_path)
  grey = img.convert('L')
  for th in range(lower,high,seg):
    temp = grey.point(lambda x: 255 if x > th else 0)
    pic_name = os.path.join(file_path,str(th) + '_' + os.path.basename(pic_path))
    temp.save(pic_name)

def test_file(pic_file,new_file='./new_pic/',th=127):
  import os,shutil
  from PIL import Image
  # 指定阈值二值化文件夹所有图片，并默认保存为 new_pic,阈值为127
  if os.path.exists(new_file):
    shutil.rmtree(new_file)
  os.mkdir(new_file)

  pic_lst = os.listdir(pic_file)
  for i,pic in enumerate(pic_lst):
    try:
      pic_path = os.path.join(pic_file,pic)
      img = Image.open(pic_path)
    except:
      print(pic)
      continue
    grey = img.convert('L')
    temp = grey.point(lambda x: 255 if x > th else 0)
    pic_name = os.path.join(new_file,os.path.basename(pic_path))
    temp.save(pic_name)
    print('\rcurrent degree is:{},total is:{}'.format(i+1,len(pic_lst)),end='')

test_file('./yanzhengma/',th=150)