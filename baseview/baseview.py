# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 20:05
# @Author  : 
# @File    : baseview.py
# @Software: PyCharm
from aw import common
from model import  Model
from appium import webdriver
from config import desired_caps
from time import sleep
import time
import os
import subprocess
import platform

class BaseView(object):
    def __init__(self,driver):
        self.driver = driver

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # def startActivity(self,activity = '',):
    #     '''启动应用'''
    #     app_package,app_activity = activity.split('/')
    #     self.driver.start_activity(app_package,app_activity)
    # def getclasses(self,classname,index = 0):
    #     buttons = self.driver.find_elements_by_class_name(classname)
    #     return buttons[index]



# PLATFOR_MNAME = 'Android'
# PLATFORM_VERSION = os.popen('adb shell getprop ro.build.version.release').read()
# print(PLATFORMVERSION)
# DEVICE_NAME = os.popen('adb shell getprop ro.boot.serialno').read()
# print(DEVICENAME)
# APP_PACKAGE = 'com.bloom.selfie.camera.beauty'#'com.wallpaper.background.hd'#
# APP_ACTIVITY = 'com.bloom.selfie.camera.beauty.module.main.SplashActivity'#'com.wallpaper.background.hd.main.SplashActivity'#

# p = subprocess.Popen('appium > appium1.log',shell=True,cwd=Model.logdirpath )
# desired_caps = {
#     "deviceName": "127.0.0.1:62001",
#     "platformName": "Android",
#     # "appPackage": "com.coolapk.market",
#     # "appActivity": "com.coolapk.market.view.main.MainActivity",
#     'noReset': 'true',
#     # 'automationName': 'UiAutomator2'
# }
# # 连接
# MD = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# MD.start_activity("com.coolapk.market","com.coolapk.market.view.main.MainActivity")
# driver.implicitly_wait(3)
#
# print(p.pid)
# print(dir(MD))
# input('============================')
# common.logcatIosKill(p.pid)
# class BaseView:
#     def __init__(self,driver):
#         self.driver = driver
#         print(self.driver)
