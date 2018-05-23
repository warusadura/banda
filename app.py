#! /usr/bin/env python3

from os import getcwd 
from threading import Thread
from flask import Flask, render_template
from selenium import webdriver
from driver import getPath, profile
from rss import get_articles 

def banda_server():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html", articles=get_articles())

    @app.route("/test")
    def user():
        return render_template("temp.html")

    app.run(threaded=True)

def banda_ui():
    ui = webdriver.Firefox(firefox_profile=profile(),
            executable_path=getPath())
    #ui.refresh()
    ui.get("http://localhost:5000")

def main():
    server_thread = Thread(target=banda_server)
    ui_thread = Thread(target=banda_ui)

    server_thread.start()
    ui_thread.start()

if __name__ == "__main__":
    main()
