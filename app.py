#! /usr/bin/env python3

from threading import Thread
from flask import Flask, render_template
from selenium import webdriver
from driver import getPath

def banda_server():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/user/<name>")
    def user(name):
        return "<h2>hello {}</h2>".format(name)

    app.run(threaded=True)

def banda_ui():
    ui = webdriver.Firefox(executable_path=getPath())
    ui.get("http://localhost:5000")

def main():
    server_thread = Thread(target=banda_server)
    ui_thread = Thread(target=banda_ui)

    server_thread.start()
    ui_thread.start()

if __name__ == "__main__":
    main()
