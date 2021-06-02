# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_firebase.py
# @Software: PyCharm

from aw import common
from model import Model
from baseview import BaseView


class Testnoxmobi():

    ''' setup  '''
    def test_setup(self):
        common.clickByAccessibilityId('NoxmobiDemo')
        common.wait(1)
        common.clickByAccessibilityId('Interstital示例')
        common.wait(1)
        common.clickByAccessibilityId('Init + SetDelegate')
        # common.wait(1)
        # common.clickByXpath('//XCUIElementTypeStaticText[@name="Init + SetDelegate"]')
        common.wait(10)
        common.clickByAccessibilityId('Show')
        common.clickByXpath('//XCUIElementTypeStaticText[@name="Show"]')
        text = common.getValueById('Test mode')
        print(text,'===========')
        common.wait(10)
        common.clickByLocation(10,30)
        print('通过坐标点击=========================')
        # common.goBack(5)
        common.wait(5)

        common.quit()
        # common.checkValue(text == 'Test mode')

