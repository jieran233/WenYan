import feedparser# pip install feedparser


# 蓝点网RSS
def landiannews():
    url = "https://www.landiannews.com/feed"
    feed = feedparser.parse(url)
    news = ""
    for i in range(0, len(feed.entries)-1):
        news = news + feed.entries[i].title + "。"
    return(news)