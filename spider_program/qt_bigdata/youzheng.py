# -*- coding:utf-8 -*-
import requests
import bs4,re,os,shutil
import traceback
import pandas as pd 

from bs4 import BeautifulSoup
from datetime import datetime


def getHtmlText(url):
  domain = 'http://www.moc.gov.cn/tongjishuju/youzheng'
  url = os.path.join(domain,url)
  print(url)
  try:
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print('requests fail!')
    return None

def getlinks(html):
  links = []
  soup = BeautifulSoup(html,'html.parser')
  infos = soup('a',title=re.compile(r'.*?邮政行业运行情况'))
  for tag in infos:
    if isinstance(tag,bs4.element.Tag):
      link = tag['href'].strip('./')
      links.append(link)
  return links

def getTableinfo(link):
  html = getHtmlText(link)
  soup = BeautifulSoup(html,'html.parser')
  year = re.search(r'20\d{2}',soup.title.string).group(0)
  tables = soup('table',border="1")
  return year,tables # table tag list

def tableProcess(tag):
  inflst =[]
  for tr in tag.tbody.children:
    row = []
    if isinstance(tr,bs4.element.Tag):
      for td in tr('td'):
        row.append(td.text.strip())
      inflst.append(row)
  return inflst

def table1Process(tag):
  inflst = tableProcess(tag)
  if inflst[0][0] == '':
    month = input("plese input month:")
  else:
    month = re.search(r'\d{1,2}',inflst[0][2]).group(0)
  print('current month:',month)
  name,val = [],[]
  inflst = inflst[2:]
  for lst in inflst:
    try:
      name.append(lst[0])
      val.append(lst[3])
    except:
      pass
  return month,name,val

def table2Process(tag):
  inflst = tableProcess(tag)
  inflst = inflst[1:]

  name,VolVal,IncVal = [],[],[]
  for lst in inflst:
    name.append(lst[0])
    VolVal.append(lst[1])
    IncVal.append(lst[3])

  tem1 = pd.DataFrame()
  tem2 = pd.DataFrame()
  tem1[0] = VolVal
  tem1.index = name
  tem2[0] = IncVal
  tem2.index = name

  return tem1,tem2

def table3Process(tag):
  inflst = tableProcess(tag)

  name1,name2,val1,val2 = [],[],[],[]
  for lst in inflst:
    name1.append(lst[1])
    name2.append(lst[4])
    val1.append(lst[2])
    val2.append(lst[5])

  name,t1 = name1[1:],name2[1:]
  name.extend(t1)

  val,t2 = val1[1:],val2[1:]
  val.extend(t2)

  tem = pd.DataFrame()
  tem[0] = val
  tem.index = name

  return tem

def table4Process(tag):
  inflst = tableProcess(tag)

  name1,name2,val1,val2 = [],[],[],[]
  for lst in inflst:
    name1.append(lst[1])
    name2.append(lst[4])
    val1.append(lst[2])
    val2.append(lst[5])

  name,t1 = name1[1:],name2[1:]
  name.extend(t1)

  val,t2 = val1[1:],val2[1:]
  val.extend(t2)

  tem = pd.DataFrame()
  tem[0] = val
  tem.index = name
  
  return tem

if __name__ == '__main__':
  picpath = '/Users/gengyanpeng/Desktop/123'
  if os.path.exists(picpath):
    shutil.rmtree(picpath)
    os.mkdir(picpath)
  else:
    os.mkdir(picpath)
  os.chdir(picpath)


  yzVal = []

  fsVol = pd.DataFrame()
  fsInc = pd.DataFrame()

  ctVolVal = pd.DataFrame()
  ctIncVal = pd.DataFrame()

  ind = True

  for i in range(4):
    if i==0:
      url = 'index.html'
    else:
      url = 'index_'+str(i)+'.html'
    html = getHtmlText(url)
    links = getlinks(html)
    for link in links:
      try:
        year,tables = getTableinfo(link)
        month,name,val = table1Process(tables[0])
        yzVal.append([name,val])

        VolVal,IncVal = table2Process(tables[1])
        if ind:
          fsVol = VolVal.copy()
          fsVol.columns = [year+'-'+month]
          fsInc = IncVal.copy()
          fsInc.columns = [year+'-'+month]
        else:
          fsVol[year+'-'+month] = VolVal.ix[:,0]
          fsInc[year+'-'+month] = IncVal.ix[:,0]
    
        Val = table3Process(tables[2])
        if ind:
          ctVolVal = Val.copy()
          ctVolVal.columns = [year+'-'+month]
        else:
          ctVolVal[year+'-'+month] = Val.ix[:,0] 

        Inc = table4Process(tables[3])
        if ind:
          ctIncVol = Inc.copy()
          ctIncVol.columns = [year+'-'+month]
        else:
          ctIncVol[year+'-'+month] = Inc.ix[:,0]
      except:
        pass

      ind = False

fsVol.to_csv('fsVol.csv')
fsInc.to_csv('fsInc.csv')
ctVolVal.to_csv('ctVolVal.csv')
ctIncVal.to_csv('ctIncVal.csv')




# yibian
i=0
url = 'index.html'
html = getHtmlText(url)
links = getlinks(html)

link = links[2]
html = getHtmlText(link)
soup = BeautifulSoup(html,'html.parser')
year = re.search(r'20\d{2}',soup.title.string).group(0)
print(year)
tables = soup('table',border="1")

# table1
table = tables[0]
inflst =[]
for tr in table.tbody.children:
  if isinstance(tr,bs4.element.Tag):
    row = []
    for td in tr('td'):
      row.append(td.text.strip())
    inflst.append(row)
print(inflst)
month = re.search(r'\d+?',inflst[0][2]).group(0)

name,val = [],[]
for lst in inflst:
  name.append(lst[0])
  val.append(lst[3])

tem1 = pd.DataFrame()
tem2 = pd.DataFrame()
tem1[year+'-'+month] = name[2:]
tem2[year+'-'+month] = val[2:]


# table2
table = tables[1]
inflst =tableProcess(table)
inflst = inflst[1:]

name,val1,val2 = [],[],[]
for lst in inflst:
  name.append(lst[0])
  val1.append(lst[1])
  val2.append(lst[3])

tem1 = pd.DataFrame()
tem2 = pd.DataFrame()
tem1[0] = val1
tem1.index = name
tem2[0] = val2
tem2.index = name

return name,tem1,tem2

fsName = pd.DataFrame()
fsVol1 = pd.DataFrame()
fsVol2 = pd.DataFrame()

fsName[year+'-'+month] = name[2:]
fsVol1[year+'-'+month] = val1[2:]
fsVol2[year+'-'+month] = val2[2:]


# table3
table = tables[2]
inflst =[]
for tr in table.tbody.children:
  if isinstance(tr,bs4.element.Tag):
    row = []
    for td in tr('td'):
      row.append(td.text.strip())
    inflst.append(row)
print(inflst)

name1,name2,val1,val2 = [],[],[],[]
for lst in inflst:
  name1.append(lst[1])
  name2.append(lst[4])
  val1.append(lst[2])
  val2.append(lst[5])

ctName = pd.DataFrame()
ctVol = pd.DataFrame()

t1,t2 = name1[1:],name2[1:]
t1.extend(t2)
ctName[year+'-'+month] = t1
t1,t2 = val1[1:],val2[1:]
t1.extend(t2)
ctVol[year+'-'+month] = t1 

# table4
table = tables[3]
inflst =[]
for tr in table.tbody.children:
  if isinstance(tr,bs4.element.Tag):
    row = []
    for td in tr('td'):
      row.append(td.text.strip())
    inflst.append(row)

name1,name2,val1,val2 = [],[],[],[]
for lst in inflst:
  name1.append(lst[1])
  name2.append(lst[4])
  val1.append(lst[2])
  val2.append(lst[5])

ctName = pd.DataFrame()
ctVol = pd.DataFrame()

t1,t2 = name1[1:],name2[1:]
t1.extend(t2)
ctName[year+'-'+month] = t1
t1,t2 = val1[1:],val2[1:]
t1.extend(t2)
ctVol[year+'-'+month] = t1 


