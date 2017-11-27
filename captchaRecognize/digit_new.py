# -*- coding:utf-8 -*-
'''
根据字符批量生成验证码：有正负，3，4，5 位
  由于考虑随机性太麻烦，为简单 分开考虑
  屏幕一共可显示 7 位

生成图片命名方式：序号_标签.jpg
'''
from __future__ import print_function
import os
from PIL import Image,ImageFilter
import numpy as np
import glob
from multiprocessing import Pool

# 字符路径
char_path = './digits_new/'# 版本二字符路径

pic_5 = os.listdir(char_path)[5]
print('子图名称：',pic_5) # 如果非文件夹中图片需要修改
houz = os.path.splitext(pic_5)[1]  # 后缀
pj_size = Image.open(char_path + '0' + houz).size
print('合成前子图尺寸:',pj_size)
new_size = 6*pj_size[0],pj_size[1]

def gen_3(target):
  # 生成 3 位的随机数
  name = []
  img = Image.open(char_path + 'bl' + houz)  # blank left
  target.paste(img, (0, 0, pj_size[0], pj_size[1]))# 将image复制到target的指定位置中

  img = Image.open(char_path + 'bc' + houz)  # blank center
  target.paste(img, (pj_size[0], 0, 2*pj_size[0], pj_size[1]))# 将image复制到target的指定位置中

  if '-' == np.random.choice(['+','-']):
    name.append('-')
    img = Image.open(char_path + 'fc' + houz)
    target.paste(img, (2*pj_size[0], 0, 3*pj_size[0], pj_size[1]))# 将image复制到target的指定位置中
  else:
    img = Image.open(char_path + 'bc' + houz)
    target.paste(img, (2*pj_size[0], 0, 3*pj_size[0], pj_size[1]))# 将image复制到target的指定位置中

  for i in range(3):
    num = str(np.random.choice(range(10)))
    name.append(num)
    img = Image.open(char_path + num + houz)
    target.paste(img,box=(pj_size[0]*(i+3), 0, pj_size[0]*(i+4), pj_size[1]))
  return name,target

def gen_4(target):
  # 生成 4 位的随机数
  name = []
  img = Image.open(char_path + 'bl' + houz)  # blank left
  target.paste(img, (0, 0, pj_size[0], pj_size[1]))# 将image复制到target的指定位置中

  if '-' == np.random.choice(['+','-']):
    name.append('-')
    img = Image.open(char_path + 'fc' + houz)
    target.paste(img, (1*pj_size[0], 0, 2*pj_size[0], pj_size[1]))# 将image复制到target的指定位置中
  else:
    img = Image.open(char_path + 'bc' + houz)
    target.paste(img, (1*pj_size[0], 0, 2*pj_size[0], pj_size[1]))# 将image复制到target的指定位置中

  for i in range(4):
    num = str(np.random.choice(range(10)))
    name.append(num)
    img = Image.open(char_path + num + houz)
    target.paste(img,box=(pj_size[0]*(i+2), 0, pj_size[0]*(i+3), pj_size[1]))
  return name,target

def gen_5(target):
  # 生成 5 位的随机数
  name = []

  if '-' == np.random.choice(['+','-']):
    name.append('-')
    img = Image.open(char_path + 'fl' + houz)
    target.paste(img, (0, 0, pj_size[0], pj_size[1]))# 将image复制到target的指定位置中
  else:
    img = Image.open(char_path + 'bl' + houz)
    target.paste(img, (0, 0, pj_size[0], pj_size[1]))# 将image复制到target的指定位置中

  for i in range(5):
    num = str(np.random.choice(range(10)))
    name.append(num)
    img = Image.open(char_path + num + houz)
    target.paste(img,box=(pj_size[0]*(i+1), 0, pj_size[0]*(i+2), pj_size[1]))
  return name,target

def gen_new():
  new_size = 7*pj_size[0],pj_size[1]
  ty = np.random.choice([3,4,5])
  target = Image.new('RGB', new_size)
  img = Image.open(char_path + 'br' + houz)  # blank right
  target.paste(img, (6*pj_size[0], 0, new_size[0], new_size[1]))# 将image复制到target的指定位置中
  if ty == 3:
    name,target = gen_3(target)
  elif ty == 4:
    name,target = gen_4(target)
  else:
    name,target = gen_5(target)
  # quality_value = 50 # quality来指定生成图片的质量，范围是0～100
  img = Image.open(char_path + 'dot.jpg')
  # target.paste(img, (945, 485))
  target.paste(img, (940, 550))
  # 对图片进行变换
  rank = np.random.choice([0.4,0.6,0.8])
  target = target.point(lambda p:p*rank)   # 对图片亮度进行随机调节 np.random.choice([0.5,1,2,3,4])
  # target = target.point(lambda p:p*np.random.choice([0.5,1,2,3,4])) # 将rank 放入可生成彩色图片
  target = target.filter(ImageFilter.GaussianBlur(radius=np.random.choice(range(2,7)))) # 对图片在 2-7 进行随机模糊化
  target = target.rotate(np.random.choice(range(-20,20))) # 对图片在 20 度内进行随机旋转
  target = target.resize((160,60))# .convert("L")

  return ''.join(name),np.asarray(target)

def main():
  # method1 循环产生样本
  for i in range(50):
    gen_new(i)

  # method2 并行产生样本
  # pool = Pool()
  # pool.map(gen_pic,range(1000))
  # pool.close()
  # pool.join()
if __name__ == '__main__':
  # 图片保存路径
  save_path = '/Users/gengyanpeng/Desktop/gen_digit/'
  # save_path = '/Volumes/MOVE/deep_learning/tensorflow/czc_ocr_pic_data/s_val/'
  if not os.path.exists(save_path):
    os.mkdir(save_path)
  # method1 循环产生样本
  for i in range(1000):
    text, image = gen_new()
    # print(text,image.shape)
    # pic_path = os.path.join(save_path,str(i) + '_' + text + houz)
    pic_path = os.path.join(save_path,text + '_' + str(i) + houz)
    Image.fromarray(image).save(pic_path,quality=100)

# 变换
# pic = '/Users/gengyanpeng/Desktop/gen_digit/11_5_-41540.jpg'
# target = Image.open(pic)  # blank right
# img = Image.open('/Users/gengyanpeng/weiyun/Python/OCR/czc_ocr/digits_2nd/dot.jpg')
# target.paste(img, (4*237, 500))
# target.show()



