# -*- coding: utf-8 -*-
from baseview.baseview import BaseView
from appium import webdriver
from config import desired_caps

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

md = BaseView(driver)
