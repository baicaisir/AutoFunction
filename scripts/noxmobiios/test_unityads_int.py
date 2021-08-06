# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_admob_int.py
# @Software: PyCharm

import logging
from aw import common, Noxmobisdk
from model import Noxmobi, Model


class Testnoxmobi:
    """ setup  """

    def setup_class(self):
        logging.info('这是开始执行动作')
        # common.setWinProxy()
        common.changeFileContent('system = (.*)', r'"UnityAds", 5, "ios"', Model.proxypath)
        self.pid = common.openMitmdump()
        common.wait(10)
        self.pid1 = common.logcatIos(Model.firebaselog)

    def test_int_show(self):
        logging.info('启动NoxmobiDemo')
        Noxmobisdk.openFirebaseButton()
        common.goBack(1)
        """ int请求"""
        common.clickById(Noxmobi.interbutton.id)
        common.clickById(Noxmobi.interbutton.init)
        common.wait(15)
        common.clickById(Noxmobi.interbutton.show)
        common.wait(15)
        common.clickCenter()
        common.wait(2)
        common.activateApp(Noxmobi.bundle_id.bundleid)
        common.swipeDown()
        common.clickById(Noxmobi.unityads.adclosename)

    def test_int_nox_sdk_request(self):
        """nox_sdk_request广告请求打点"""
        inter = common.logBlockKeywordExist(Model.int_nox_sdk_request, Model.firebaselog)
        assert inter

    def test_int_nox_sdk_waterfall(self):
        inter = common.logBlockKeywordExist(Model.int_nox_sdk_waterfall_request, Model.firebaselog)
        assert inter

    def test_int_nox_sdk_show(self):
        inter = common.logBlockKeywordExist(Model.int_nox_sdk_show, Model.firebaselog)
        assert inter

    def test_int_nox_sdk_click(self):
        inter = common.logBlockKeywordExist(Model.int_nox_sdk_click, Model.firebaselog)
        assert inter

    def test_int_nox_sdk_show_failed(self):
        Noxmobisdk.checkFailedMsg()

    def teardown(self):
        pass

    def teardown_class(self):
        logging.info('这是结尾清除动作')
        common.terminateApp(Noxmobi.bundle_id.bundleid)
        # common.quit()
        common.logcatIosKill(self.pid)
        common.logcatIosKill(self.pid1)
