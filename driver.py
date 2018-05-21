#! /usr/bin/env python3

import os
from selenium import webdriver

def getPath():
    return os.getcwd() + "/geckodriver"

def no_script():
    # disable javascript
    profile = webdriver.FirefoxProfile()
    profile.set_preference("javascript.enabled", False)
    return profile
