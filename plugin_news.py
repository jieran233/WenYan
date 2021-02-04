import requests
import json
from urllib.parse import quote


# 微博热搜榜
def wbtop(top=10):
    url = "https://v1.alapi.cn/api/new/wbtop"
    payload = "num="+str(top)
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data=payload, headers=headers)
    dic = json.loads(response.text)['data']
    hotwords = ""
    for i in range(0,len(dic)-1):
        hotwords = hotwords + dic[i]['hot_word'] + "；"
    return(hotwords.rstrip("；"))


# 历史上的今天
def eventHistory(monthday='', type_='event'):
    url = "https://v1.alapi.cn/api/eventHitory"
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data="", headers=headers)
    dic = json.loads(response.text)['data']
    events = ""
    for i in range(0,len(dic)-1):
        if dic[i]['type'] == type_:
            monthday_ = dic[i]['monthday']
            date = str(dic[i]['year']) + "年" + str(monthday_)[0:2].strip('0') + "月" + str(monthday_)[2:4].strip('0') + "日"
            events = events + date + "，" + dic[i]['title'] + "。"
    return(events.rstrip("。"))