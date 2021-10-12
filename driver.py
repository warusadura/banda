#! /usr/bin/env python3

from os import getcwd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options, FirefoxProfile


def getPath():
    return getcwd() + "/geckodriver"


def profile():
    opts = Options()
    #opts.binary = binary

    #privacy protecting preferences
    opts.preferences.update({
        "javascript.enabled": False,
        "browser.tabs.drawInTitlebar": True,
        "browser.privatebrowsing.autostart": True,
        "privacy.donottrackheader.enabled": True,
        "geo.enabled": False,
        "network.http.sendRefererHeader": 0,
        "dom.event.clipboardevents.enabled": False,
        "media.autoplay.enabled": False,
        "extensions.pocket.enabled": False,
        "dom.battery.enabled": False,
        "device.sensors.enabled": False,
        "beacon.enabled": False,
        "media.peerconnection.enabled": False,
        "webgl.disabled": True,
        "network.http.sendRefererHeader": 0,
        "privacy.firstparty.isolate": True,
        "network.cookie.lifetimePolicy": 2,
    })

    capabilities = DesiredCapabilities.FIREFOX.copy()
    profile = webdriver.FirefoxProfile(getcwd() + "/profile")
    return [opts, capabilities, profile]
