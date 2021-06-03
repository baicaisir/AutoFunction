# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 20:05
# @Author  : 
# @File    : baseview.py
# @Software: PyCharm
import time

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

    def findByAccessibilityId(self,idname):
        """iOS通过name定位"""
        d = self.driver.find_element_by_accessibility_id(idname)
        return d

    def findElementsByAccessibilityId(self,idname):
        """iOS通过name定位"""
        d = self.driver.find_elements_by_accessibility_id(idname)
        return d

    def findByXpath(self,xpath):
        """通过xpath定位"""
        d = self.driver.find_element_by_xpath(xpath)
        return d

    def wait(self,n):
        """等待时长，默认一秒"""
        self.driver.implicitly_wait(n)
        return time.sleep(n)

    def tapByLocation(self,x,y):
        """通过坐标点击"""
        # 获取当前手机屏幕大小X,Y
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        print('当前屏幕尺寸为（%s,%s）'%(X,Y))
        return self.driver.execute_script("mobile: tap", {"x": x , "y": y})

    def clickCenter(self):
        """点击屏幕中心位置"""
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        return self.driver.execute_script("mobile: tap", {"x": X/2, "y": Y/2})

    def goBack(self):
        """返回键"""
        return self.driver.back()

    def quit(self):
        """设备退出"""
        return self.driver.quit()