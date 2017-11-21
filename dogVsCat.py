# coding:utf8
from __future__ import print_function
import os
import subprocess
import shutil
import random


def gen_filelist(txt_path,pic_path):
  with open(txt_path,'w+') as f:
    for pic in os.listdir(pic_path):
      if 'cat' in pic:
        f.write(pic+' 0\n')
      elif 'dog' in pic:
        f.write(pic + ' 1\n')
      else:
        print(pic)
        continue

def gen_lmdb(pic_fpath,txt_path,lmdb_fpath):
  convert_exe = '/home/qt/caffe/build/tools/convert_imageset'
  param1 = "--shuffle --resize_height=128 --resize_width=128"

  cmd = ' '.join([convert_exe,param1,pic_fpath,txt_path,lmdb_fpath])
  print(cmd)
  # subprocess.Popen(cmd,shell=True)
  os.system(cmd)

def extract_test(pic_path,copy_path):
  for i in range(1250):
    raw_path = pic_path + 'cat.' + str(random.randrange(1,12499)) + '.jpg'
    new_path = raw_path.replace('train','test')
    shutil.copy(raw_path,new_path)

  for i in range(1250):
    raw_path = pic_path + 'dog.' + str(random.randrange(1,12499)) + '.jpg'
    new_path = raw_path.replace('train','test')
    shutil.copy(raw_path,new_path)


def del_mean(lmdb_fpath,output):
  computeMean = '/home/qt/caffe/build/tools/compute_image_mean'
  cmd = ' '.join([computeMean,lmdb_fpath,output])
  os.system(cmd)

if __name__ == '__main__':
  train_pic_fpath = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/train/'
  train_txt_path = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/train.txt'
  train_mean_output = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/mean.binaryproto'

  test_pic_fpath = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/test/'
  test_txt_path = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/test.txt'


  # gen test
  # extract_test(train_pic_fpath,test_pic_fpath)

  # gen train.txt test.txt
  # gen_filelist(train_txt_path,train_pic_fpath)
  # gen_filelist(test_txt_path,test_pic_fpath)

  # trans jpg to lmdb
  train_lmdb_fpath = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/catdog_train_lmdb'
  test_lmdb_fpath = '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/catdog_test_lmdb'
  # gen_lmdb(test_pic_fpath,test_txt_path,test_lmdb_fpath)
  # del_mean(train_lmdb_fpath,train_mean_output)

  # train model
  caffe_train = '/home/qt/caffe/build/tools/caffe train --solver='
  solver_path =  '/home/qt/Documents/gyp/deep_learning/deeplearn_data/caffe_dog/pb/solver.prototxt'
  os.system(caffe_train + solver_path)



