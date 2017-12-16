# coding=utf8

import re,random,json,time,os,requests
from requests.compat import str as rstr
import urllib,shelve,hashlib,lxml.html
import traceback,six
from six.moves.urllib.parse import urlparse
import pdb

store_path = './images'

dft_hdrs = {
  # 'Pragma': 'no-cache',
  # 'Cache-Control': 'no-cache',
  'Accept': 'text/plain, */*; q=0.01',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
  # 'Referer': 'http://www.creditchina.gov.cn/search_all',
  'Accept-Encoding': 'gzip, deflate',
  # 'Origin':'http://www.creditchina.gov.cn',
  # 'Cookie':'Hm_lvt_0076fef7e919d8d7b24383dc8f1c852a=1468301399; 
  # Hm_lpvt_0076fef7e919d8d7b24383dc8f1c852a=1468393252',
  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
}

img_api_url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj\
&ct=201326592&is=&fp=result&queryWord={0}\
&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=2&ic=&word={0}\
&s=&se=&tab=&width=0&height=0&face=&istype=&qc=&nc=1&fr=&pn={1}&rn=30&gsm=3c&{2}='


charests = ('utf8', 'gbk', 'gb2312', 'big5', 'ascii','shift_jis', 'euc_jp', 
  'euc_kr', 'iso2022_kr','latin1', 'latin2', 'latin9', 'latin10', 'koi8_r',
  'cyrillic', 'utf16', 'utf32') 


_fd = shelve.open('urls')
def filterduplicate(url):
    global _fd
    if url in _fd:
        return False
    _fd[url] = 1

    return True

vare = {
    'w': "a",
    'k': "b",
    'v': "c",
    '1' : "d",
    'j': "e",
    'u': "f",
    '2' : "g",
    'i': "h",
    't': "i",
    '3' : "j",
    'h': "k",
    's': "l",
    '4' : "m",
    'g': "n",
    '5' : "o",
    'r': "p",
    'q': "q",
    '6' : "r",
    'f': "s",
    'p': "t",
    '7' : "u",
    'e': "v",
    'o': "w",
    '8' : "1",
    'd': "2",
    'n': "3",
    '9' : "4",
    'c': "5",
    'm': "6",
    '0' : "7",
    'b': "8",
    'l': "9",
    'a': "0",
    '_z2C$q': ":",
    "_z&e3B": ".",
    'AzdH3F': "/"
}


def uncompile(url):
    if url.startswith('http'):
        return url

    url = url.replace('_z2C$q', ':').replace('_z&e3B', '.').replace('AzdH3F', '/')
    url = ''.join([vare.get(s, s) for s in url])

    return url

def str_encode(stri, encoding='utf8'):
    if isinstance(stri, unicode):
        return stri.encode(encoding)
    else:
        for i in charests:
            try:
                return stri.decode(i).encode(encoding)
            except:
                pass
        else:
            return stri


def get_filename(url, ct=None):
    # Content-Type:image/gif
    upd = urlparse(url) 
    fn = os.path.basename(upd.path)
    fn = str_encode(fn)

    ext = os.path.splitext(fn)
    if ext[1]:
        ext = ext[1]
    else:
        if ct and 'image/' in ct:
            ext = '.'+ct.split('/')[-1]
        else:
            ext = ''

    m = hashlib.md5()
    m.update(url)
    nfn = m.hexdigest()  

    fn = os.path.join(STORE_PATH, '%s%s' % (nfn, ext))

    return os.path.normpath(os.path.realpath(fn))


def get_doc(resp):
    content = None

    if isinstance(resp, six.string_types):
        content = resp

    else:
        encoding = resp.encoding

        if not resp.content:
            # content = str('')
            return None

        # Fallback to auto-detected encoding.
        if resp.encoding is None or resp.encoding == 'ISO-8859-1':
            encoding = resp.apparent_encoding

        # Decode unicode from given encoding.
        try:
            content = rstr(resp.content, encoding, errors='replace')
        except (LookupError, TypeError):
            content = rstr(resp.content, errors='replace')

    doc = lxml.html.document_fromstring(content)
    if getattr(resp, 'url'):
        doc.make_links_absolute(doc.base_url or resp.url)
    return doc


def get_resp(url):
  hdrs = dft_hdrs.copy()
  kw = {'timeout':10,'headers':hdrs}
  try:
    resp = requests.get(url,**kw)
  except:
    return
  return resp


def save_progress(key, pn):
    db = shelve.open('progress')
    db[key] = pn
    db.close()

def get_progress(key):
    db=shelve.open('progress')
    try:
        return int(db[key])
    except:
        return 0
    db.close()



def get_page(keyword):
  # 获取每个关键词对应的所有图片
  kw = urllib.request.quote(keyword)
  url = entry_url.format(kw)

  resp = get_resp(url)
  if resp is None:
    return

  cur_store_path = os.path.join(store_path,keyword)
  if not os.path.exists(cur_store_path):
    os.mkdir(cur_store_path)

  html = resp.text
  pic_re = 'objURL":"([a-z.:/_A-Z0-9]*)"'
  image_urls = re.findall(pic_re,html)

  for url in image_urls:
    get_image(url)

def get_image(url):
  resp = get_resp(url)
  if resp not None:
    try:
      ct = resp.headers.get()



entry_url = 'http://image.baidu.com/search/index?&tn=baiduimage&word={0}'


if __name__ == "__main__":
  store_path = '~/Desktop/images'
  if not os.path.exists(store_path):
    os.mkdir(store_path)
  

  keywords = ['美女']
  for key in set(keywords):
    get_page(key)

