#! /usr/bin/env python3

from urllib import request
from bs4 import BeautifulSoup

subreddits = [
	"https://old.reddit.com/r/cscareerquestions/hot/.rss",
	"https://www.reddit.com/r/Python/hot/.rss",
	"https://old.reddit.com/r/programming/.rss",
]

def pickup_reddit():
    reddit_data = []
    for subreddit in subreddits:
        req = request.Request(subreddit)
        req.add_header("User-Agent", "36435")
        with request.urlopen(req) as reddit:
            data = BeautifulSoup(reddit, "xml")
            reddit_data.append(data)

    raw_posts = []
    for source in reddit_data:
        raw_posts.extend(source.find_all("entry"))

    posts = []
    for single in raw_posts:
        post = {
                "title": single.title.string,
                "link": single.link["href"],
                "category": single.category["term"]
               }
        posts.append(post)

    return posts
