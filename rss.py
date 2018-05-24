#! /usr/bin/env python3

from urllib import request
from bs4 import BeautifulSoup

feeds = [
        "https://news.ycombinator.com/rss",
        "https://www.wired.com/feed/category/security/latest/rss",
        "https://hackernoon.com/feed",
        "https://arstechnica.com/feed/",
        ]

def reddit():
    # identify reddit rss feeds
    # https://old.reddit.com/r/cscareerquestions+Python/hot/.rss
    isreddit = False
 

def pickup():
    # create individual articles
    rss_data = []
    for feed in feeds:
        with request.urlopen(feed) as rss:
            data = BeautifulSoup(rss, "xml")
            rss_data.append(data)

    raw_articles = []
    for source in rss_data:
        raw_articles.extend(source.find_all("item"))

    articles = []
    state = True
    for article in raw_articles:
        if article.comments is None:
            state = False

        item = {
            "title": article.title.string,
            "link": article.link.string,
            "comments": article.comments.string if state else None
            }
        articles.append(item)
   # print(articles)
    return articles
