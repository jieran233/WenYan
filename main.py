import requests
import json
from urllib.parse import quote
import time

import plugin_daily as daily
import plugin_news as news
import plugin_rss as rss

# 发送留言方法
def submit(content, classesId, toAccountIds, toAccountIdsName, toAccountId_id_show, toAccountId_name_show, captcha, geli_yuser, geli_yschool, geli_session, remember_usr):
    url = "https://apps.32k12.com/ecloud/ymessage/create.do"
    payload = "id=&status=1&r_classesId="+classesId+"&q_eq_type_i=2&toAccountId_name=&toAccountId_id=&toAccountIds="+toAccountIds+"&toAccountIdsName="+quote(toAccountIdsName,'utf-8')+"&toAccountId_id_show="+quote(toAccountId_id_show,'utf-8')+"&toAccountId_name_show="+quote(toAccountId_name_show,'utf-8')+"&app_code_1612184765242=99&content="+quote(content,'utf-8')+"&attachmentId="
    headers = {'accept':"application/json, text/javascript, */*; q=0.01", 'accept-encoding':"gzip, deflate, br", 'accept-language':"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", 'content-type':"application/x-www-form-urlencoded; charset=UTF-8", 'cookie':"captcha="+captcha+"; geli-yuser="+geli_yuser+"; geli-yschool="+geli_yschool+"; geli-session="+geli_session+"; remember_usr="+remember_usr, 'dnt':"1", 'origin':"https://apps.32k12.com", 'referer':"https://apps.32k12.com/ecloud/ymessage/create.do?placeValuesBefore", 'sec-fetch-dest':"empty", 'sec-fetch-mode':"cors", 'sec-fetch-site':"same-origin", 'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41", 'x-requested-with':"XMLHttpRequest"}
    response = requests.request("POST", url, data=payload, headers=headers)
    return(response.text)


# # 按指定长度分段切割字符串或列表
# # 参考资料 https://blog.csdn.net/qq_26373925/article/details/101135611
# def cut(obj, sec):
#     return [obj[i:i+sec] for i in range(0,len(obj),sec)]


# 填写参数
classesId = "135797"
toAccountIds = "6899229"
toAccountIdsName = "岳锦天同学"
toAccountId_id_show = "6899229;"
toAccountId_name_show = "岳锦天同学;"
# 填写Cookie
captcha = "859d51c4abb855a3-7a3f577d1773d6e07c378c344784118866997796"#[该Cookie需保持最新(浏览会话结束时到期)]
geli_yuser = "4851022"
geli_yschool = "4214"
geli_session = "6fabadb86aca92e10e99a51ac5bf2e8f"#[该Cookie需保持最新(浏览会话结束时到期)]
remember_usr = "13910137227"
# 填写发送内容（手动分条）
contents = ["早上好，又是新的一天~    每日一言："+daily.hitokoto()+"    "+daily.tenki('石家庄')+"    "+daily.covid19('河北')+"    "+daily.covid19('北京'), "微博热搜TOP20："+news.wbtop(20), "蓝点网资讯："+rss.landiannews(), "历史上的今天："+news.eventHistory()]
# 发送留言并输出返回结果
for i in range(0,len(contents)):
    # 倒序分条发送
    j = len(contents)-i-1
    num = '('+str(j+1)+'/'+str(len(contents))+')'
    print(num)
    print(submit(num+contents[j], classesId, toAccountIds, toAccountIdsName, toAccountId_id_show, toAccountId_name_show, captcha, geli_yuser, geli_yschool, geli_session, remember_usr))
    # 延时1秒，防止顺序错误或被服务端ban
    time.sleep(1)

# # 服务端要求内容长度必须在1到500个字符之间
# # 处理发送内容，大于500字符则分条发送
# if len(content.encode()) > 500:
#     print("[info] 发送内容大于500字符，将采用分条发送")
#     content_parts = cut(content.encode(),500)
#     # print(content_parts)
#     for i in range(0,len(content_parts)-1):
#         print(content_parts[i].decode())
#         # print("发送消息 (part"+str(i)+"/"+str(len(content_parts))+")："+submit(, classesId, toAccountIds, toAccountIdsName, toAccountId_id_show, toAccountId_name_show, captcha, geli_yuser, geli_yschool, geli_session, remember_usr))
# else:
#     print("[info] 发送内容获取完毕，即将发送")
#     print(submit(content, classesId, toAccountIds, toAccountIdsName, toAccountId_id_show, toAccountId_name_show, captcha, geli_yuser, geli_yschool, geli_session, remember_usr))
