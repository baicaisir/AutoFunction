from baseview.baseview import BaseView
from appium import webdriver
from time import sleep

desired_caps = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  # "appPackage": "com.coolapk.market",
  # "appActivity": "com.coolapk.market.view.main.MainActivity",
  'noReset': 'true'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

md = BaseView(driver)
