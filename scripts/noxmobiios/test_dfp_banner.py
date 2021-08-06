# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_admob_banner.py
# @Software: PyCharm

import logging
from aw import common, Noxmobisdk
from model import Noxmobi, Model


class Testnoxmobi:
    """ setup  """

    def setup_class(self):
        logging.info('这是开始执行动作')
        # common.setWinProxy()
        common.changeFileContent('system = (.*)', r'"GoogleDFP", 4, "ios"', Model.proxypath)
        self.pid = common.openMitmdump()
        common.wait(10)
        self.pid1 = common.logcatIos(Model.firebaselog)

    def test_banner_show(self):
        logging.info('启动NoxmobiDemo')
        Noxmobisdk.openFirebaseButton()
        common.goBack(1)
        """ banner请求"""
        common.clickById(Noxmobi.bannerbutton.id)
        common.clickById(Noxmobi.bannerbutton.init)
        common.wait(10)
        common.clickById(Noxmobi.bannerbutton.show)
        common.wait(3)

    def test_banner_nox_sdk_request(self):
        """nox_sdk_request广告请求打点"""
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_request, Model.firebaselog)
        assert banner

    def test_banner_nox_sdk_waterfall(self):
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_waterfall_request, Model.firebaselog)
        assert banner

    def test_banner_nox_sdk_show(self):
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_show, Model.firebaselog)
        assert banner

    def test_banner_nox_sdk_show_failed(self):
        Noxmobisdk.checkFailedMsg()

    #
    # def test_banner_nox_sdk_click(self):
    #     banner = common.logBlockKeywordExist(Model.banner_nox_sdk_click, Model.firebaselog)
    #     assert banner

    def teardown(self):
        pass

    def teardown_class(self):
        logging.info('这是结尾清除动作')
        common.terminateApp(Noxmobi.bundle_id.bundleid)
        # common.quit()
        common.logcatIosKill(self.pid)
        common.logcatIosKill(self.pid1)

