def a():
	# 图片下载实例 1
	# -*- coding:utf-8 -*-

	from urllib import request

	# 获取图片文件对象 response
	url = 'http://placekitten.com/g/500/300'
	# response = urllib.urlopen(url)
	req = request.Request(url)	# 发送一个请求
	response = request.urlopen(req)
	cat_img = response.read()	# 读取图片
	with open('cat1.jpg','wb') as f:
		f.write(cat_img)	# 将图片以 二进制 写入 cat1.jpg
	print (response.geturl())	# 访问具体链接地址
	print (response.info())	# http messge 对象，含远程服务器 header 信息等
	print (response.getcode())# 状态代码，200 表示 ok，404 表示 页面不存在

def b():
	# 图片下载实例 2 
	'''
	将猫奴网站图片，随机下载一些到本地桌面123 文件夹
	技术路线：使用 urllib 库的下载函数
	'''
	# -*- coding:utf-8 -*-
	import os
	import urllib
	# def savepic(url,picname):
	# 	try:
	# 		r = requests.get(url)
	# 		r.raise_for_status
	# 		with open(picname,'wb') as f:
	# 			f.write(r.content)
	# 	except:
	# 		pass

	picpath = '/Users/gengyanpeng/Desktop/123'
	if not os.path.exists(picpath):
		os.mkdir(picpath)
	os.chdir(picpath)

	for i in range(1,20):
		pic_url = 'http://placekitten.com/g/' + str(50*i)+ '/' + str(25*i)
		picname = str(50*i) + '_' + str(25*i) + '.jpg'
		# savepic(pic_url,picname)
		urllib.request.urlretrieve(pic_url,picname)

def a1():
	# 图片下载实例 3 
	'''
	下载某一贴吧上面图片
	'''
	# -*- coding:utf-8 -*-
	import os,urllib
	import requests
	from bs4 import BeautifulSoup
	import bs4
	def getHtmlText(url):
		try:
			r = requests.get(url)
			r.raise_for_status
			r.encoding = r.apparent_encoding
			return r.text
		except:
			return ''

	def downloadpic(html):
		count = 0
		soup = BeautifulSoup(html,'html.parser')
		for tag in soup('img',{'class':'BDE_Image','pic_ext':"jpeg"}):
			if isinstance(tag,bs4.element.Tag):
				count +=1
				piclink = tag['src']
				picname = piclink.split('/')[-1]
				# savepic(piclink,picname)
				urllib.request.urlretrieve(piclink,picname)
				print('\r已下载：%d'%count,end ='')
		print('\n')

	picpath = '/Users/gengyanpeng/Desktop/123'
	if not os.path.exists(picpath):
		os.mkdir(picpath)
	os.chdir(picpath)

	for i in range(1,4):
		url = 'https://tieba.baidu.com/p/2772656630?pn=' + str(i)
		html = getHtmlText(url)
		print('第%d页图片下载中...'%i)
		downloadpic(html)

def a4():
	# 图片下载实例 4
	'''
	下载煎蛋网上的妹子图
	'''
	# -*- coding:utf-8 -*-
	import os,urllib
	import requests
	from bs4 import BeautifulSoup
	import bs4,time
	def getHtmlText(url,header={'User-Agent':'Mozilla/5.0'}):
		try:
			r = requests.get(url,headers = header)
			r.raise_for_status
			r.encoding = r.apparent_encoding
			return r.text
		except:
			return ''

	def downloadmm(url):
		count = 0
		html = getHtmlText(url)
		soup = BeautifulSoup(html,'html.parser')
		for tag in soup('img',{'src':re.compile(r'^//.*?\.jpg')}):
			if isinstance(tag,bs4.element.Tag):
				count += 1
				picname = tag['src'].split('/')[-1]
				urllib.request.urlretrieve('http:'+tag['src'],picname)
				print('\r已下载：%d'%count,end ='')
		print('\n')

	url = 'http://jandan.net/ooxx'
	picpath = '/Users/gengyanpeng/Desktop/123'
	if not os.path.exists(picpath):
		os.mkdir(picpath)
	os.chdir(picpath)
	html = getHtmlText(url)
	soup = BeautifulSoup(html,'html.parser')
	curpagenum = eval(soup.find('span',{'class':'current-comment-page'}).string)[0]
	for i in range(curpagenum,0,-1):
		page_url = url + '/page-' + str(i)
		print('正在下载第%d页'%i)
		downloadmm(page_url)
		# time.sleep(1)


a()