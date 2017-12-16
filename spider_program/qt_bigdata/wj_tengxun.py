import requests
import json
import numpy as np 

def tijiao():
  url = "https://wj.qq.com/sur/collect_answer"

  payload = {'survey_id':'1480739',
  'answer_survey':'''{"id":"1480739","survey_type":0,"jsonLoadTime":28,"ldw":"142BBF2B-5585-42B9-9D07-781C0930A2C3","time":1501665850,"ua":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36","openid":"",
  "pages":[{"id":"1",
  "questions":[{"id":"q-1-HaSI","type":"radio","text":"",
  "options":[{"id":"o-100-ABCD","checked":0,"text":""},{"id":"o-101-EFGH","checked":0,"text":""},{"id":"o-2-TJOC","checked":0,"text":""},{"id":"o-3-h5AN","checked":0,"text":""},{"id":"o-4-xotX","checked":1,"text":"<p>数据预处理部</p>"},{"id":"o-5-tmUv","checked":0,"text":""}],"blanks":[]},
  {"id":"q-2-VSUC","type":"text","text":"耿延鹏","options":[],"blanks":[]},
  {"id":"q-9-lF27","type":"textarea","text":"17826853236","options":[],"blanks":[]},
  {"id":"q-5-THSi","type":"text","text":"4","options":[],"blanks":[]},
  {"id":"q-6-wYgH","type":"text","text":"1","options":[],"blanks":[]},
  {"id":"q-7-P0r0","type":"text","text":"5","options":[],"blanks":[]},
  {"id":"q-8-knsd","type":"text","text":"3","options":[],"blanks":[]}]}],"referrer":""}'''}

# 发文数
# 朋友圈
# 点赞
# 评论

  response = requests.request("POST", url, data=payload)

  print(response.text)
  print(json.loads(response.text)['info'])

if __name__ == '__main__':
  tijiao()