#! /usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options, FirefoxProfile

def getPath():
    return os.getcwd() + "/geckodriver"

def profile():
    profile_path = os.getcwd() + "/profile"
    #options = Options()
    firefox = webdriver.FirefoxProfile(profile_directory=profile_path)
    #options.add_argument("-profile")
    #options.add_argument(profile_path)
    
    # remove javascript
    #firefox.set_preference("javascript.enabled", 0)
    # remove title bar
    #firefox.set_preference("browser.tabs.drawInTitlebar", True)
    #firefox.set_preference("browser.privatebrowsing.autostart", True)
    #firefox.set_preference("geo.enabled", False)
    #firefox.set_preference("reader.parse-on-load.force-enabled", True)
    #firefox.set_preference("reader.color_scheme", "light")
    #firefox.set_preference("browser.reader.detectedFirstArticle", False)
    #firefox.set_preference("extensions.pocket.enabled", False)
    return firefox
