import feedparser# pip install feedparser

# RSSHub 域名
global rsshub
rsshub = "https://rsshub-4girn3oa300d0127-1256554206.ap-shanghai.app.tcloudbase.com/"# 自建的RSS服务


# RSS订阅源爬取通用方法
def rssfeed(url, len_=0, break_=" || "):
    feed = feedparser.parse(url)
    news = ""
    if len_ == 0:
        len__ = len(feed.entries)-1
    else:
        len__ = len_
    for i in range(0, len__):
        news = news + feed.entries[i].title + break_
    # print(len(news.encode()))
    return(news.rstrip(break_))


# 蓝点网RSS
def landiannews():
    return(rssfeed("https://www.landiannews.com/feed", 5))

# 百度搜索风云榜-实时热点
def baidutop():
    return(rssfeed(rsshub + "/baidu/topwords/1", 10))

# StuartRiki_KeyTV 的 bilibili 动态
def keytvnews():
    return(rssfeed(rsshub + "/bilibili/user/dynamic/39471072/", 2))

# 酷安图文-编辑精选
def coolapkpy():
    return(rssfeed(rsshub + "/coolapk/tuwen", 10))

# Bangumi放送列表
def bangumi():
    feed = feedparser.parse(rsshub + "/bangumi/calendar/today")
    bangumi = ""
    for i in range(0, len(feed.entries)-1):
        # idx = feed.entries[i].title.index("｜") + 1
        # bangumi = bangumi +"《"+ feed.entries[i].title[idx:] + "》"
        bangumi = bangumi +"《"+ feed.entries[i].title + "》"
    # print(len(bangumi.encode()))
    return(bangumi)