#! /usr/bin/env python3

import os
from selenium import webdriver

def getPath():
    return os.getcwd() + "/geckodriver"

def get_profile():
    profile = webdriver.FirefoxProfile()
    # remove javascript
    profile.set_preference("javascript.enabled", False)
    # remove title bar
    profile.set_preference("browser.tabs.drawInTitlebar", True)
    #profile.set_preference("browser.suppress_first_window_animation",False)

    return profile
