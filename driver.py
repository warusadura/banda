#! /usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options, FirefoxProfile

def getPath():
    return os.getcwd() + "/geckodriver"

def create_profile():
    profile_path = os.getcwd() + "/profile"
    #options = Options()
    profile = webdriver.FirefoxProfile(profile_directory=profile_path)
    #options.add_argument("-profile")
    #options.add_argument(profile_path)
    
    # remove javascript
    profile.set_preference("javascript.enabled", False)
    # remove title bar
    profile.set_preference("browser.tabs.drawInTitlebar", True)
    return profile
