# author: jieran233
# BUGs:
# 1. cookie到期，返回{"statusCode":301, "message":"会话超时，请重新登录。","backUrl":"/login.jsp"}
#    解决方法: 服务端打开浏览器保持登录32k12，登录后粘贴最新的cookie
#    (留言页面为 https://apps.32k12.com/ecloud/ymessage/list.do)
#    (共2个cookie需保持最新，分别为captcha和geli-session)
#    (这2个cookie均为 浏览会话结束时 到期)
# 2. 留言无法换行
#    解决方法：暂无

import requests
import json
from urllib.parse import quote
import plugin_test

# 发送留言方法
def submit(content, classesId, toAccountIds, toAccountIdsName, toAccountId_id_show, toAccountId_name_show, captcha, geli_yuser, geli_yschool, geli_session, remember_usr):
    url = "https://apps.32k12.com/ecloud/ymessage/create.do"
    payload = "id=&status=1&r_classesId="+classesId+"&q_eq_type_i=2&toAccountId_name=&toAccountId_id=&toAccountIds="+toAccountIds+"&toAccountIdsName="+quote(toAccountIdsName,'utf-8')+"&toAccountId_id_show="+quote(toAccountId_id_show,'utf-8')+"&toAccountId_name_show="+quote(toAccountId_name_show,'utf-8')+"&app_code_1612184765242=99&content="+quote(content,'utf-8')+"&attachmentId="
    headers = {'accept':"application/json, text/javascript, */*; q=0.01", 'accept-encoding':"gzip, deflate, br", 'accept-language':"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", 'content-type':"application/x-www-form-urlencoded; charset=UTF-8", 'cookie':"captcha="+captcha+"; geli-yuser="+geli_yuser+"; geli-yschool="+geli_yschool+"; geli-session="+geli_session+"; remember_usr="+remember_usr, 'dnt':"1", 'origin':"https://apps.32k12.com", 'referer':"https://apps.32k12.com/ecloud/ymessage/create.do?placeValuesBefore", 'sec-fetch-dest':"empty", 'sec-fetch-mode':"cors", 'sec-fetch-site':"same-origin", 'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41", 'x-requested-with':"XMLHttpRequest"}
    response = requests.request("POST", url, data=payload, headers=headers)
    return(response.text)


# 填写参数
classesId = "135797"
toAccountIds = "6899229"
toAccountIdsName = "岳锦天同学"
toAccountId_id_show = "6899229;"
toAccountId_name_show = "岳锦天同学;"
# 填写Cookie
captcha = "21983c78d4c60cc1196b669a1773d746d6956fd-21404404562400024"#[该Cookie需保持最新(浏览会话结束时到期)]
geli_yuser = "4851022"
geli_yschool = "4214"
geli_session = "64eb3a415340431415651e32dc8b4cc0"#[该Cookie需保持最新(浏览会话结束时到期)]
remember_usr = "13910137227"
# 填写发送内容
content = "早上好，又是新的一天~ 每日一言："+plugin_test.hitokoto()+"。\n"+plugin_test.tenki("石家庄")+"\n"+plugin_test.covid19("河北")+"。\n"+plugin_test.covid19("北京")+"。\n——由『闻言』发送"
# 发送并输出返回结果
print(submit(content, classesId, toAccountIds, toAccountIdsName, toAccountId_id_show, toAccountId_name_show, captcha, geli_yuser, geli_yschool, geli_session, remember_usr))