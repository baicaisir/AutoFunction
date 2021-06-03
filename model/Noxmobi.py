# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 11:05 上午
# @Author  : 
# @File    : Noxmobi.py
# @Software: PyCharm

class Noxmobi:
    class closebutton(object):
        id = 'Close Advertisement'

    class settingbutton(object):
        id = '设置页'

    class interbutton(object):
        id = 'Interstital示例'

    class bannerbutton(object):
        id = 'Banner示例'

    class rewardbutton(object):
        id = 'RewardVideo示例'

    class testmodebutton(object):
        name = 'Test Mode'
        xpath = '//XCUIElementTypeSwitch[@name="Test Mode"]ß'

    class firebasebutton(object):
        name = 'Friebase'
        xpath = '//XCUIElementTypeSwitch[@name="Firebase"]'

    class rcbutton(object):
        name = 'RC 初始化'
        xpath = '//XCUIElementTypeSwitch[@name="RC 初始化"]'

