# -*- coding:utf-8 -*-
"""
爬取 搜狐娱乐信息
"""
import requests

url = "http://ent.163.com/special/000380VU/newsdata_tv_07.js"

querystring = {"callback":"data_callback"}

headers = {
    'upgrade-insecure-requests': "1",
    'x-devtools-emulate-network-conditions-client-id': "d777652e-341a-4bb2-9e28-a15f60477569",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "usertrack=ZUcIhVh9cguSfxyEA9+pAg==; _ntes_nnid=441a7bba8e3267f314b94ca8339afd22,1484616206727; _ntes_nuid=441a7bba8e3267f314b94ca8339afd22; mail_psc_fingerprint=1a31e1607fd7f94fbd0b7667768629d3; vjuids=-4ec8a4e1d.15a8dcb7a93.0.a371231448495; NTES_REPLY_NICKNAME=gengyanpeng12%40163.com%7Cgengyanpeng12%7C%7C%7C%7CsmAhDikcmTtBRdJo7ygTXheUBeoZ4aYULfVRqyelBSPe8Ftg8d_0OT2d6WMGmLEZO_bfWOPsYlziQ.cSkrmoJLxvZAxwXuUaYrWPmpaUyMKu.%7C1%7C-1; NTES_CMT_USER_INFO=96586564%7Cgengyanpeng12%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CZ2VuZ3lhbnBlbmcxMkAxNjMuY29t; __gads=ID=9ab52d125af11854:T=1492519912:S=ALNI_Mbp3pZfI_9CzUHyEc0XpnoTGa4oXQ; UM_distinctid=15b811e86b754d-0d8acb26df48ea-396a7807-13c680-15b811e86b8b75; __s_=1; ANTICSRF=d3b76c35f743e714cefe20c47cb0685c; NTES_SESS=eyyXKTX1ZTkyQXUSyCHN2SMVP.y6xGQUtiGrp6__AF7EKp8LKuA4P3nuNkFdjDCSPFJ.YKNWd3xIp43jVx8V.gNPbFxwH_MvoyHHISra6G4VtdBPDJP1GzHHJJJpiDPo5pkUD50D0CPcLgWbSLax0ufSK6jw0c0u5umWIeduaSbmxZzZEKaVKHnG4; S_INFO=1503325574|0|0&80##|gengyanpeng12||neteasemail_android; P_INFO=gengyanpeng12@163.com|1503325574|0|mail163|00&99|zhj&1503325571&mail_client#zhj&330100#10#0#0|&0|mailsettings&neteasemail_android&mail163_qrcode&lmlc_check|gengyanpeng12@163.com; _qddaz=QD.44cmw6.ae8ouu.j6x50c6f; _ga=GA1.2.1269062543.1484616212; vjlast=1492519919.1505221398.11; ne_analysis_trace_id=1505221398332; vinfo_n_f_l_n3=cf7a5ea30c4619c5.1.0.1502511350770.0.1505221518897; s_n_f_l_n3=cf7a5ea30c4619c51502511350770; __utma=187553192.1269062543.1484616212.1505293254.1505560971.13; __utmc=187553192; __utmz=187553192.1505560971.13.6.utmcsr=demo.pyspider.org|utmccn=(referral)|utmcmd=referral|utmcct=/task/1:3925c4494da347ea2429a1c5a1b0cb77; __oc_uuid=02c770c0-0a17-11e7-a257-ff0beaf94fbd",
    'cache-control': "no-cache",
    'postman-token': "ecf1cba0-7cfd-3e3a-c5ac-3cef21eaccf0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response.encoding = response.apparent_encoding

# print(response.text)

dt_lst = eval(re.search(r'\[.*\]',re.sub(r'[\s|\n]','',response.text)).group())
for dt in dt_lst:
  print(dt)