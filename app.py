#! /usr/bin/env python3
 
from threading import Thread
from flask import Flask, render_template
from selenium import webdriver
from driver import getPath, profile
from rss import pickup

def banda_server():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html", articles=pickup())

    @app.route("/blogs")
    def blog():
        return render_template("blog.html")

    @app.route("/events")
    def events():
        return render_template("event.html")

    @app.route("/reddit")
    def reddit():
        return render_template("reddit.html")

    app.run(threaded=True)

def banda_ui():
    ui = webdriver.Firefox(options=profile()[0],
            capabilities=profile()[1],
            firefox_profile=profile()[2],
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
