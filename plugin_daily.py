import requests
import json
from urllib.parse import quote


# 取中间文本函数
# 参考资料 https://blog.csdn.net/u013291301/article/details/106630644
def take_middle_text(txt,txt_s,txt_e='',seeks=0,seeke=0):
    try:
        if txt_e or seeks or seeke:
            pass
        else:
            raise 1
        s_1 = txt.find(txt_s)
        if s_1 == -1:
            raise 1
        l_1 = len(txt_s)
        if txt_e:
            s_2 = txt.find(txt_e,s_1)
            if s_1 == -1 or s_2 == -1:
                return False
            return txt[s_1+l_1:s_2]
        if seeks:
            return txt[s_1-seeks:s_1]
        if seeke:
            return txt[s_1+l_1:s_1+l_1+seeke]
    except:
        return '传参错误或未找到传参文本'


# 一言
def hitokoto():
    url = "https://v1.hitokoto.cn"
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    # GET请求，指定了url和headers
    response = requests.get(url, headers=headers)
    # print(response.text)

    # json.loads()方法可以把json转换为python字典
    dic = json.loads(response.text)
    # 声明一言类型数组
    cType = ["动画","漫画","游戏","文学","原创","来自网络","其他","影视","诗词","网易云","哲学","抖机灵"]
    # ord()方法可以把ASCII字符转成对应在ASCII表中的序号
    # 小写字母在表中的位置从97开始，减去97即数组的第一个成员cType[0]
    cNum = ord(dic["type"])-97
    return("["+cType[cNum]+"] "+dic["hitokoto"]+"——"+dic["from"])


# 天气
def tenki(city):
    url = "https://v1.alapi.cn/api/tianqi/now"
    # 指定城市，需URL编码
    payload = "city=" + quote(city, 'utf-8')
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    # POST请求，指定了url,data,和headers
    response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)

    # json.loads()方法可以把json转换为python字典
    dic = json.loads(response.text)
    return(dic["data"]["city"]+"今日天气(更新于"+dic["data"]["update_time"]+")："+dic["data"]["wea"]+"，气温"+dic["data"]["tem2"]+"℃~"+dic["data"]["tem1"]+"℃"+"，"+dic["data"]["win"]+dic["data"]["win_speed"]+"("+dic["data"]["win_meter"]+")，"+"湿度"+dic["data"]["humidity"]+"，能见度"+dic["data"]["visibility"]+"，气压"+dic["data"]["pressure"]+"hPa，空气质量指数"+dic["data"]["air"]+"("+dic["data"]["air_level"]+")，"+dic["data"]["air_tips"])


# 疫情数据
# 参考资料 https://blog.csdn.net/ymx12349/article/details/113191611
def covid19(province):  
    url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=' + quote(province, 'utf-8')
    html = requests.get(url)
    data = json.loads(html.text)['data']
    for i in data:
        data1={}
        data1['日期']=str(i['year'])+'年'+i['date'][0:2]+'月'+i['date'][3:5]+'日'
        data1['省份']=i['province']

        data1['新增确诊']=i['newConfirm']
        data1['新增无症状感染者']=i['wzz_add']
        data1['新增治愈']=i['newHeal']
        data1['新增死亡']=i['newDead']

        data1['累计确诊']=i['confirm']
        data1['累计无症状感染者']=i['wzz']
        data1['累计治愈']=i['heal']
        data1['累计死亡']=i['dead']

    return(data1['省份']+"昨日新增确诊病例"+str(data1['新增确诊'])+"例，新增无症状感染者"+str(data1['新增无症状感染者'])+"例，新增治愈病例"+str(data1['新增治愈'])+"例，新增死亡病例"+str(data1['新增死亡'])+"例")