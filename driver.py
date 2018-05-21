#! /usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def getPath():
    return os.getcwd() + "/geckodriver"

def create_profile():
    profile_path = os.getcwd() + "/profile"
    options = Options()
    options.add_argument("-profile")
    options.add_argument(profile_path)
    
    profile = webdriver.FirefoxProfile()
    # remove javascript
    profile.set_preference("javascript.enabled", False)
    # remove title bar
    profile.set_preference("browser.tabs.drawInTitlebar", True)
    return options
