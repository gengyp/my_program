# -*- coding:utf-8 -*-
'''
生成简单四位数字图片 命名方式：序号_标签.jpg
例：123_5263.jpg
'''
from __future__ import print_function
import os
from PIL import Image,ImageFilter
import numpy as np
# import glob
# from multiprocessing import Pool


# 图片保存路径
save_path = '/Users/gengyanpeng/Desktop/gen_digit/'
# 生成图片张数
pic_num = 1000

# 字符路径
char_path = './digits_old/'  # 源字符路径
houz = '.jpg'  # 后缀
pj_size = Image.open(char_path + '0' + houz).size
print('合成前子图尺寸:',pj_size)
new_size = 6*pj_size[0],pj_size[1]
print('合成后全图尺寸:',new_size)

def gen_old():
  target = Image.new('RGB', new_size) # 合成图
  img = Image.open(char_path + 'b' + houz)
  target.paste(img, (0, 0, pj_size[0], pj_size[1]))# 将image复制到target的指定位置中
  target.paste(img, (5*pj_size[0], 0, new_size[0], pj_size[1]))# 将image复制到target的指定位置中

  name = []

  for i in range(4):
    num = str(np.random.choice(range(10)))
    name.append(num)
    img = Image.open(char_path + num +houz)  # .resize((40,95))
    box = (pj_size[0]*(i+1), 0, pj_size[0]*(i+2), pj_size[1])
    target.paste(img,box=box) # 将image到target的指定位置中
    quality_value = 50 # quality来指定生成图片的质量，范围是0～100

  rank = np.random.choice([0.5,0.8,1,1.5,2])
  target = target.point(lambda p:p*rank)   # 对图片亮度进行随机调节 np.random.choice([0.5,1,2])
  # target = target.point(lambda p:p*np.random.choice([0.5,1,2,3,4])) # 将rank 放入可生成彩色图片
  target = target.filter(ImageFilter.GaussianBlur(radius=np.random.choice(range(2,6)))) # 对图片在 2-7 进行随机模糊化
  target = target.rotate(np.random.choice(range(-20,20))) # 对图片在 20 度内进行随机旋转
  target = target.resize((160,60)) # .convert("L")
  return ''.join(name),np.asarray(target)


if __name__ == '__main__':
  if not os.path.exists(save_path):
    os.mkdir(save_path)
  # method1 循环产生样本
  for i in range(pic_num):
    text, image = gen_old()
    # print(text,image.shape)
    pic_path = os.path.join(save_path,str(i)+ '_' + text + houz)
    Image.fromarray(image).save(pic_path)

  # method2 并行产生样本
  # pool = Pool()
  # pool.map(gen_pic,range(100))
  # pool.close()
  # pool.join()


# 单张图片变换测试
# pic = '/Users/gengyanpeng/Desktop/gen_digit/11_5_-41540.jpg'
# target = Image.open(pic)  # blank right
# img = Image.open('/Users/gengyanpeng/weiyun/Python/OCR/czc_ocr/digits_2nd/dot.jpg')
# target.paste(img, (4*237, 500))
# target.show()



