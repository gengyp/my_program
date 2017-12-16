#-*- coding: utf-8 -*-
import urllib,urllib2,json
'''
post 向服务器提交未处理的数据，get 向服务器请求数据
urlopen 中 参数data 被赋值，则以 post 方式提交
服务器通过 request headers 判断是否非人类访问，故可修改 headers 隐藏
为了避免访问频率过快：1、延迟访问时间 2、代理 ip
'''
# content = raw_input('Please input to the content of the translation:')
# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
# data = {}
# data['type'] = 'AUTO'
# data['i'] = content
# data['doctype'] = 'json'
# data['xmlVersion'] = '1.8'
# data['keyfrom'] = 'fanyi.web'
# data['ue'] = 'UTF-8'
# data['action'] = 'FY_BY_CLICKBUTTON'
# data['typoResult'] = 'true'
# # 将 data 用函数转化成urlopen可读对象,unicode文件格式 编码成 utf-8编码
# data = urllib.urlencode(data).encode('utf-8')
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# head = {'User-Agent':user_agent}
# # 隐藏访问对象:修改 headers ，缺点：无法避免访问频率屏蔽
# req = urllib2.Request(url,data,headers = head)
# response = urllib2.urlopen(req)
# # utf-8 编码形式的文件，将其解码成 unicode 形式
# html = response.read().decode('utf-8')
# target = json.loads(html)
# print u'result is :%s' % target['translateResult'][0][0]['tgt']
# print req.headers	#


# python2
import urllib,urllib2,json,time

while True:
	content = raw_input('请输入翻译内容(输入"q!"退出程序):')
	if content == 'q!':
		break
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
	data = {'action': 'FY_BY_CLICKBUTTON',
	'doctype': 'json',
	'i': content,
	'keyfrom': 'fanyi.web',
	'type': 'AUTO',
	'typoResult': 'true',
	'ue': 'UTF-8',
	'xmlVersion': '1.8'}
	data = urllib.urlencode(data).encode('utf-8')
	req = urllib2.Request(url,data)
	# print url

	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	req.add_header('User-Agent',user_agent)

	response = urllib2.urlopen(req)
	html = response.read().decode('utf-8')
	target = json.loads(html)
	print u'result is :%s' % target['translateResult'][0][0]['tgt']
	# time.sleep(1)	# 延迟 2s 钟


# # python3
# import requests
# header = {'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
#           'Accept-Encoding':'gzip, deflate',
#           'Accept-Language':'zh-CN,zh;q=0.8',
#           'Connection':'keep-alive',
#           'Cookie':'gs_b_tas=BZQX5HP6DY6RHY29; JSESSIONID=A94E177971954E1A44827352D4F2C8F6',
#           'Host':'xyxx.zjzwfw.gov.cn',
#           'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=http://fanyi.youdao.com/'
# payload = {'i':'苹果',
#  'from':'AUTO',
#  'to':'AUTO',
#  'smartresult':'dict',
#  'client':'fanyideskweb',
#  'salt':'1499862804311',
#  'sign':'d74e4b732b3ecc5dc50d40cb6320a38f',
#  'doctype':'json',
#  'version':'2.1',
#  'keyfrom':'fanyi.web',
#  'action':'FY_BY_ENTER',
#  'typoResult':'true'}

# r = requests.post(url,data=payload)
# r.text

