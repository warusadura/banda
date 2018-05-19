#! /usr/bin/env python3

from flask import Flask
from selenium import webdriver
import driver

app = Flask(__name__)
ui = webdriver.Firefox(executable_path=driver.path)

@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.run(threaded=True)
    ui.get("http://localhost:5000")
