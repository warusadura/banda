#! /usr/bin/env python3

from urllib import request
from bs4 import BeautifulSoup

url = "https://www.wired.com/feed/category/security/latest/rss"
with request.urlopen(url) as rss:
    data = BeautifulSoup(rss, "xml")

raw_articles = data.find_all("item")
articles = []

for article in raw_articles:
    item = {
            "title": article.title.string,
            "description": article.description.string,
            "link": article.link.string
            }
    articles.append(item)

def get_articles():
    return articles
