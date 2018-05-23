#! /usr/bin/env python3

from urllib import request
from bs4 import BeautifulSoup

feeds = [
        "https://www.wired.com/feed/category/security/latest/rss",
        "https://news.ycombinator.com/rss",
        ]

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
    state = False
    for article in raw_articles:
        if article.comments:
            state = True
        item = {
            "title": article.title.string,
            "description": article.description.string,
            "link": article.link.string,
            "comments": article.comments.string if state else ""
            }
        articles.append(item)
    return articles
