# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/7/14 9:24
"""
import pandas as pd 
import os,glob,re 
import numpy as np 

root = 'C:/Users/qt_52/Desktop/'
path = root + 'p2p_data/*.txt'

def opentxt(path):
  with open(path,'r',encoding='utf-8') as f:
    dt = eval(f.read())
  return dt

def generate_dt(lst):
  dt = {}
  for d in lst:
    dt[d['key'].strip()] = d['value']
  return dt 


month_info = []
year_info = []
row_name = ['成交量（万元）', '参考收益率（%）', '投资人数（个）', '借款人数（个）']
year_row = ['成交量','当日待还余额（万元）-30日平均', '当日待还余额（万元）', '资金净流入（万元）']
qx_colname = ['1月标', '2月标','3月标','4-6月标','6-12月标']
col_name = ['平台名称']
col_name.extend(qx_colname)
qx_df = pd.DataFrame(columns=col_name)
count = 0
for file in glob.glob(path):
  # print(file)
  dt = opentxt(file)
  p2p_name = re.search(r'\d+?_(.*)?\.txt',file).group(1)
  # print(p2p_name)
  # month data process
  for i in range(4):
    m_row = [p2p_name,row_name[i]]
    m_row.extend(dt['basicValue']['y%s'%(i+1)])
    month_info.append(m_row)
  # year data process
  y_row = [p2p_name,year_row[0]]
  y_row.extend(dt['amountValue'])
  year_info.append(y_row)

  y_row = [p2p_name,year_row[1]]
  y_row.extend(dt['moneyStockValue']['y2'])
  year_info.append(y_row)

  y_row = [p2p_name,year_row[2]]
  y_row.extend(dt['moneyStockValue']['y1'])
  year_info.append(y_row)

  y_row = [p2p_name,year_row[3]]
  y_row.extend(dt['netFlowValue'])
  year_info.append(y_row)
  
  # qixian data process
  ndt = generate_dt(dt['basicValue']['pie2'])
  qx_df.loc[count,'平台名称'] = p2p_name
  for k,v in ndt.items():
    if k in qx_df.columns:
      qx_df.loc[count,k] = v
    else:
      qx_df[k] = np.nan
      qx_df.loc[count,k] = v
  count += 1
  print(count,514)

# data save
col_name = ['平台','栏目']
col_name.extend(dt['basicValue']['x'])
df = pd.DataFrame(month_info,columns=col_name)
df.to_csv(root+'p2p_month.csv',encoding='utf-8')

col_name = ['平台名称','栏目详情']
col_name.extend(dt['date'])
df = pd.DataFrame(year_info,columns=col_name)
df.to_csv(root+'p2p_year.csv',encoding='utf-8')

qx_df.to_csv(root+'qixian_90.csv',encoding='utf-8')



