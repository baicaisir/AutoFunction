# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 20:05
# @Author  : 
# @File    : baseview.py
# @Software: PyCharm

class BaseView:
    def __init__(self,  driver):
        self.driver = driver

    def swipeUp(self,  t=500,  n=1):
        """向上滑动屏幕"""
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.5  # x坐标
        y1 = window['height'] * 0.75  # 起始y坐标
        y2 = window['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1,  y1,  x1,  y2,  t)

    def swipeDown(self,  t=500,  n=1):
        """向下滑动屏幕"""
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.5  # x坐标
        y1 = window['height'] * 0.25  # 起始y坐标
        y2 = window['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1,  y1,  x1,  y2,  t)

    def swipLeft(self,  t=500,  n=1):
        """向左滑动屏幕"""
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.75
        y1 = window['height'] * 0.5
        x2 = window['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1,  y1,  x2,  y1,  t)

    def swipRight(self,  t=500,  n=1):
        """向右滑动屏幕"""
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.25
        y1 = window['height'] * 0.5
        x2 = window['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1,  y1,  x2,  y1,  t)

    def startActivity(self, activity):
        """启动应用"""
        app_package, app_activity = activity.split('/')
        return self.driver.start_activity(app_package, app_activity)

    def getClasses(self, classname, index=0):
        """获取对应classname的属性"""
        buttons = self.driver.find_elements_by_class_name(classname)
        return buttons[index]

    def clickByid(self, idname, index):
        return self.driver.find_elements_by_id(idname)[index].click()
