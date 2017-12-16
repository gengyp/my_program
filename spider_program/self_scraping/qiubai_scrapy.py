# -*- coding:utf-8 -*-
'''
# 获取糗事百科热门段子的 发布人，性别，段子内容，以及评论数
'''
import requests
from bs4 import BeautifulSoup
import bs4,re
import traceback

#糗事百科爬虫类
class QSBK(object):
  #初始化方法，定义一些变量
  def __init__(self):
    self.pageIndex = 1
    #初始化headers
    self.header = {'User-Agent':'Mozilla/5.0'}
    #存放段子的变量，每一个元素是每一页的段子
    self.stories = []
    #存放程序是否继续运行的变量
    self.enable = False

  #传入某一页的索引获得页面代码
  def getPage(self,pageIndex):
    try:
      url = 'https://www.qiushibaike.com/hot/page/' + str(pageIndex) + '/'
      # https://www.qiushibaike.com/hot/page/2/
      #构建请求的request
      r = requests.get(url,headers = self.header)
      # r.raise_for_status
      r.encoding = r.apparent_encoding
      return r.text
    except:
      print("连接糗事百科失败")
      return

  #传入某一页代码，返回本页不带图片的段子列表
  def getPageItems(self,pageIndex):
    html = self.getPage(pageIndex)
    if not html:
      print("页面加载失败....")
      return
    #用来存储每页的段子们
    pageStories = []
    soup = BeautifulSoup(html,'lxml')
    divs = soup.select('#content-left')[0]('div',{'class':re.compile(r'article block')})
    #遍历正则表达式匹配的信息
    for div in divs:
      try:
        publisher = div.select('div.author.clearfix > a:nth-of-type(2) > h2')[0].text.strip()
        gender = div.select('div.author.clearfix > div')[0]
        content = div.select('a.contentHerf > div > span')[0].text.strip()
        happy = div.select('div.stats > span.stats-vote > i')[0].text.strip()
        comment = div.select('i')[1].text.strip()
        # pageStories.append([publisher,gender,content,happy,comment])
      except:
        print('select is error!')
        publisher = div.h2.string.strip()
        gender = re.search(r'Gender\s(.*?Icon.*?)<',str(div)).group(1).replace('Icon">',' ')
        content = div('div',{'class':'content'})[0].span.text.strip()
        happy = div('i',{'class':'number'})[0].string
        comment = div('i',{'class':'number'})[1].string
      pageStories.append([publisher,gender,content,happy,comment])
    return pageStories

  #加载并提取页面的内容，加入到列表中
  def loadPage(self):
    #如果当前未看的页数少于2页，则加载新一页
    if self.enable == True:
      if len(self.stories) < 2:
        #获取新一页
        pageStories = self.getPageItems(self.pageIndex)
        #将该页的段子存放到全局list中
        if pageStories:
          self.stories.append(pageStories)
          #获取完之后页码索引加一，表示下次读取下一页
          self.pageIndex += 1

  #调用该方法，每次敲回车打印输出一个段子
  def getOneStory(self,pageStories,page):
    #遍历一页的段子
    for story in pageStories:
      #等待用户输入
      inpt = input()
      #每当输入回车一次，判断一下是否要加载新页面
      self.loadPage()
      #如果输入Q则程序结束
      if inpt == "q!":
          self.enable = False
          return
      print('第{:,d}页\n发布人: {s[0]}\n性别年龄: {s[1]}\n内容: {s[2]}\n好笑: {s[3]}\n评论: {s[4]}'.format(page,s=story))

  #开始方法
  def start(self):
    #使变量为True，程序可以正常运行
    self.enable = True
    #先加载一页内容
    self.loadPage()
    #局部变量，控制当前读到了第几页
    nowPage = 0
    print("正在读取糗事百科,按回车查看新段子，输入:q! 退出")
    while self.enable:
      if len(self.stories)>0:
        #从全局list中获取一页的段子
        pageStories = self.stories[0]
        #当前读到的页数加一
        nowPage += 1
        #将全局list中第一个元素删除，因为已经取出
        del self.stories[0]
        #输出该页的段子
        self.getOneStory(pageStories,nowPage)

if __name__ == '__main__':
  spider = QSBK()
  spider.start()


  # import re
  # from bs4 import BeautifulSoup
  # div = BeautifulSoup(a,'lxml')
  # publisher = div.h2.string.strip()
  # gender = re.search(r'Gender\s(.*?Icon.*?)<',str(div)).group(1).replace('">',':')
  # content = div.span.text.strip()
  # happy = div('i',{'class':'number'})[0].string
  # comment = div('i',{'class':'number'})[1].string
  # story = [publisher,gender,content,comment]
  # print('发布人: {s[0]}\n性别: {s[1]}\n内容: {s[2]}\n评论数: {s[3]}'.format(s=story))

