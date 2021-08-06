# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 17:23
# @Author  : 
# @File    : test_setup.py
# @Software: PyCharm


"""创建此脚本用于调试使用，将需要调试的步骤放在step里面即可"""

import logging

from aw import common
from model import Noxmobi


class TestsetUp:
    """ setup  """

    def setup(self):
        # common.setWinProxy()
        self.pid = common.openMitmdump()
        # self.pid1 = common.logcatIos(Model.firebaselog)
        logging.info('这是一个调试脚本')

    def test_step(self):
        common.clickCenter()
        common.wait(20)
        # common.activateApp(Noxmobi.bundle_id.bundleid)
        # common.swipeDown()
        # common.clickById(Noxmobi.unityads.adclosename)

    def teardown(self):
        common.quit()
        common.logcatIosKill(self.pid)