import requests
import json
import time
import pymongo

# client = pymongo.MongoClient('localhost', 27017)
# mydb = client['mydb']
# lagou = mydb['lagou']

headers = {
    'Cookie':'JSESSIONID=ABAAABAAAGFABEF681CEC2796CF477F1433D385A01AA027; _gat=1; user_trace_token=20171216200823-d070cfca-e259-11e7-9c4f-525400f775ce; LGUID=20171216200823-d070d71d-e259-11e7-9c4f-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3Dlagou; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_hz_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; _gid=GA1.2.1676429992.1513426104; _ga=GA1.2.1906570964.1513426104; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513426104,1513426108,1513426111; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513426119; LGSID=20171216200827-d2c29e3d-e259-11e7-9c4f-525400f775ce; LGRID=20171216200838-d9621391-e259-11e7-9c4f-525400f775ce; SEARCH_ID=7ccc494f6a6d448f9f7dd7754c2a22f0',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Connection':'keep-alive'
}

def get_page(url,params):
    html = requests.post(url, data=params, headers=headers,proxies={'http': 'http://111.76.66.140:1863'})
    json_data = json.loads(html.text)
    total_Count = json_data['content']['positionResult']['totalCount']
    page_number = int(total_Count/15) if int(total_Count/15)<30 else 30
    get_info(url,page_number)

def get_info(url,page):
    for pn in range(1,page+1):
        params = {
            'first': 'true',
            'pn': str(pn),
            'kd': 'Python'
        }
        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos = {
                    'businessZones':result['businessZones'],
                    'city':result['city'],
                    'companyFullName':result['companyFullName'],
                    'companyLabelList':result['companyLabelList'],
                    'companySize':result['companySize'],
                    'district':result['district'],
                    'education':result['education'],
                    'explain':result['explain'],
                    'financeStage':result['financeStage'],
                    'firstType':result['firstType'],
                    'formatCreateTime':result['formatCreateTime'],
                    'gradeDescription':result['gradeDescription'],
                    'imState':result['imState'],
                    'industryField':result['industryField'],
                    'jobNature':result['jobNature'],
                    'positionAdvantage':result['positionAdvantage'],
                    'salary':result['salary'],
                    'secondType':result['secondType'],
                    'workYear':result['workYear']
                }
                # lagou.insert_one(infos)
                print(infos)
                time.sleep(20)
        except requests.exceptions.ConnectionError:
            pass

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first': 'true',
        'pn': '1',
        'kd': 'Python'
    }
    get_page(url,params)