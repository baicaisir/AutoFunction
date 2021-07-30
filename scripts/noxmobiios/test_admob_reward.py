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
        # common.setWinProxy()
        # self.pid = common.openMitmweb()
        self.pid1 = common.logcatIos(Model.firebaselog)

    def test_rewaid_show(self):
        logging.info('启动NoxmobiDemo')
        Noxmobisdk.openFirebaseButton()
        common.goBack(1)
        """ banner请求"""
        common.clickById(Noxmobi.bannerbutton.id)
        common.clickById(Noxmobi.bannerbutton.init)
        common.wait(10)
        common.clickById(Noxmobi.bannerbutton.show)
        common.wait(3)
        text = common.getValueById(Noxmobi.bannerbutton.testmode)
        common.checkValue(text == Noxmobi.bannerbutton.testmode)
        common.clickById(Noxmobi.bannerbutton.testmode)
        Noxmobisdk.backFromAppBar()

    def test_banner_nox_sdk_request(self):
        """nox_sdk_request广告请求打点"""
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_request, Model.firebaselog)
        assert banner

    def test_banner_nox_sdk_waterfall(self):
        logging.info('cehsi ')
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_waterfall_request, Model.firebaselog)
        assert banner

    def test_banner_nox_sdk_show(self):
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_show, Model.firebaselog)
        assert banner

    def test_banner_nox_sdk_click(self):
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_click, Model.firebaselog)
        assert banner

    def teardown(self):
        pass

    def teardown_class(self):
        common.terminateApp(Noxmobi.bundle_id.bundleid)
        common.quit()
        # common.logcatIosKill(self.pid)
        common.logcatIosKill(self.pid1)
        # common.checkValue(text == 'Test mode')

        # """ 插屏请求"""
        # # common.clickById(Noxmobi.interbutton.id)
        # common.wait(1)
        # common.clickById(Noxmobi.interbutton.init)
        # common.wait(10)
        # common.clickById(Noxmobi.interbutton.show)

        # common.wait(5)
        # common.clickCenter()
        # common.wait(5)
        # a = common.checkIdIsExist('URL')
        # print(a)
        # common.checkValue(a)

        # 通过坐标点击返回广告展示页
        # common.clickByLocation(22, 22)
        #
        # # 广告关闭按钮位置
        # logging.info('断言之后接着执行')
        # common.wait(5)
        # common.clickByLocation(20, 60)
        # common.goBack(2)
