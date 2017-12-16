import requests
import json

headers = {
    'Cookie':'ALF=1516019382; SCF=AkF5ycbpcAVkDDM3YcINVHZf0emHWolAE4AdfCmhvRYRWndsLFlajXUU5KaHhiTG2QmOHoWBbQuUPCkq5IuCZDU.; SUB=_2A253MWHmDeRhGeRJ6lAR9CvMyT-IHXVU2g-urDV6PUNbktBeLVHSkW1NUmX1fFOW-xGPzInn9pOfeJvNFDwdtF_B; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5uXaWuhFv-pQs.Oj9iyVzM5JpX5KMhUgL.FozNeKz7Sh-7eoe2dJLoIp-LxK-LBonL12eLxKqL1-eL1-ikeKzt; SUHB=08J6mkpK4zkCkY; SSOLoginState=1513427382; _T_WM=cf90849e69549be6063756b980018f40; H5_INDEX=0_all; H5_INDEX_TITLE=%E5%B8%8C%E6%9C%9B_12; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
    'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

# f = open('C:/Users/LP/Desktop/weibo.txt','a+',encoding='utf-8')

def get_info(url,page):
    html = requests.get(url,headers=headers)
    print(html.url)
    json_data = json.loads(html.text)
    card_groups = json_data[0]['card_group']
    for card_group in card_groups:
        content = card_group['mblog']['text'].split(' ')[0]+'\n'
        # f.write(content)
        # print(content)

    next_cursor = json_data[0]['next_cursor']

    if page<50:
        next_url = 'https://m.weibo.cn/index/friends?format=cards&next_cursor='+str(next_cursor)+'&page=1'
        page = page + 1
        get_info(next_url,page)
    else:
        pass
        # f.close()

if __name__ == '__main__':
    url = 'https://m.weibo.cn/index/friends?format=cards'
    get_info(url,1)
