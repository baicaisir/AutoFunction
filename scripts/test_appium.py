# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_firebase.py
# @Software: PyCharm

from aw import common
from model import Model
from baseview import BaseView


class TestNoxmobi():

    ''' setup  '''
    def test_setup(self):
        a = common.getClassProperty('android.widget.TextView',3).text
        print(a)
        common.checkValue(True)
