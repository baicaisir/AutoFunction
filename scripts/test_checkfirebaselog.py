# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_checkfirebaselog.py
# @Software: PyCharm

from aw import common
from model import Model

class Testfirebase():

    def __init__(self):
        self.wordlist = common.logBlockKeywordExist(Model.pattern, '%siphone.log' % Model.logdirpath)

    def test_check_firebase(self):

        pass

