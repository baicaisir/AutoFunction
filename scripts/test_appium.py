# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_firebase.py
# @Software: PyCharm

from aw.common import Commmon
from model import Model
from baseview import baseview


class Testfirebase(Commmon):

    '''  nox_sdk_waterfall 瀑布流请求打点  '''
    def test_banner_nox_sdk_waterfall(self):
        a = Commmon.getclass('android.widget.TextView',3).text
        print(a)
        assert a ==  '酷安'




