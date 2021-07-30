# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 16:21
# @Author  : 
# @File    : config.py
# @Software: PyCharm


desired_caps = {
  "udid":"0477289bc8bd957105d40b8552d9c79275d71334",
  "deviceName": "iPhone X",
  # "udid":"4f0a0ad893f2e9465c009b558fb633f604c178e6",
  # "deviceName": "Noxmobi 6sp",
  "platformVersion": "14.4",
  "automationName": "XCUITest",
  "platformName": "iOS",
  "newCommandTimeout": "3600",
  "skipLogCapture": "true",
  "webDriverAgentUrl": "http://127.0.0.1:8200",
  "usePrebuiltWDA": "true",
  "useXctestrunFile": "false"
}
"""
请自行配置设备情况下面的为Android的部分配置
{
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    # "appPackage": "com.coolapk.market",
    # "appActivity": "com.coolapk.market.view.main.MainActivity",
    'noReset': 'true',
    'automationName': 'UiAutomator2'
    }
"""


