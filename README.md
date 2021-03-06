<h1><center>闻言 WenYan</center></h1>
<center>实现石家庄市智慧教育云平台电子留言的自动发送</center>

![闻言.png (1544×869) (gitee.com)](https://gitee.com/jieran233/pic-bed/raw/master/闻言.png)

## 🗒 介绍

实现石家庄市智慧教育云平台电子留言的自动发送

最新版本效果图：

![2021-02-19_120607.png (1077×1625) (gitee.com)](https://gitee.com/jieran233/pic-bed/raw/master/2021-02-19_120607.png)

📜 程序基本流程如下：

```
main.py	---调用插件爬取并处理数据---> plugin_test.py

		<--返回数据----------------

		---调用接口发送留言----------------------------------->
```

🕔 目前规划为每天5:00定时发送，使用任务计划运行main.py实现

## 🔳 todo

✅ 使用Python调用石家庄市智慧教育云平台API发送留言

✅ 实现plugin

✅ 支持RSS订阅源爬取

⭕ 支持文件上传

## 🐞 BUGs

1. **[✅已解决]** cookie到期，返回`{"statusCode":301, "message":"会话超时，请重新登录。","backUrl":"/login.jsp"}`

   **📄解决方法(🔃间接):** 服务端打开浏览器保持登录32k12，登录后粘贴最新的cookie
   
   （留言页面为 [https://apps.32k12.com/ecloud/ymessage/list.do](https://apps.32k12.com/ecloud/ymessage/list.do)；共2个cookie需保持最新，分别为`captcha`和`geli-session`，这2个cookie均为浏览会话结束时到期）
   
2. **[❌未解决]** 留言无法换行

3. **[✅已解决]** 服务端要求内容长度必须在1到500个字符之间

   📄**解决方法(❌未能实现):** 自动按字数分条发送
   
   📄**解决方法(✅已实现):** 手动分条发送

😊 欢迎提交Issue；欢迎提交PR
