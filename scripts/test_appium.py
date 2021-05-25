# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_firebase.py
# @Software: PyCharm

from aw import common
from model import Model
from baseview import BaseView


class Testfirebase():

    '''  nox_sdk_waterfall 瀑布流请求打点  '''
    def test_banner_nox_sdk_waterfall(self):
        a = common.getclass('android.widget.TextView',3).text
        print(dir(a))
        print(a)
        assert a ==  '酷安'
