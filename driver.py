#! /usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.firefox.options import FirefoxProfile

def getPath():
    return os.getcwd() + "/geckodriver"

def profile():
    profile_path = os.getcwd() + "/profile"
    #options = Options()
    firefox = webdriver.FirefoxProfile(profile_directory=profile_path)
    return firefox
