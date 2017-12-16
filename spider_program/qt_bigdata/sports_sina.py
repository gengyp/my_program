# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/7/14 9:24
"""

import requests, re
from bs4 import BeautifulSoup
import pandas as pd


def getHtml(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text


def get_links():
    url = 'http://sports.sina.com.cn/'
    html = getHtml(url)
    soup = BeautifulSoup(html, 'lxml')
    # links = soup.select('body > div.content.wrap > section.ppcs.pfootballchina > div.ppcs_c.clearfix > div.ppcs_l.fl')
    # print(links,type(links),len(links))
    tags = soup('a', target="_blank", href=re.compile(r'http://sports\.sina.*?html'))
    urls = []
    for tag in tags:
        urls.append(tag['href'])
    return urls


def get_txt(url='http://sports.sina.com.cn/china/j/2017-07-13/doc-ifyiakwa4018400.shtml'):
    html = getHtml(url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        title = soup.select('#j_title')[0].text.strip()
    except:
        print(url)
        return
    tags = soup.select('#artibody')[0]('p')
    txt = []
    for tag in tags:
        txt.append(tag.text.strip())
    return title, ' '.join(txt)


if __name__ == '__main__':
    content = []
    path = r'C:\Users\qt_52\Desktop\sina_sports.csv'
    links = get_links()
    # print(links)
    for i, link in enumerate(set(links)):
        print('cur page is:', i + 1, 'total:', len(set(links)))
        tup = get_txt(link)
        if tup is None:
            continue
        content.append(tup)
    pd.DataFrame(content).to_csv(path, index=False, encoding='utf-8')
