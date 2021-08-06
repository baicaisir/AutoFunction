# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 14:33
# @Author  : 
# @File    : test_admob_reward.py
# @Software: PyCharm

import logging
from aw import common, Noxmobisdk
from model import Noxmobi, Model


class Testnoxmobi:
    """ setup  """

    def setup_class(self):
        logging.info('这是开始执行动作')
        # common.setWinProxy()
        common.changeFileContent('system = (.*)', r'"UnityAds", 3, "ios"', Model.proxypath)
        self.pid = common.openMitmdump()
        common.wait(5)
        self.pid1 = common.logcatIos(Model.firebaselog)

    def test_reward_show(self):
        logging.info('启动NoxmobiDemo')
        Noxmobisdk.openFirebaseButton()
        common.goBack(1)
        """ reward请求  """
        common.clickById(Noxmobi.rewardbutton.id)
        common.clickById(Noxmobi.rewardbutton.init)
        common.wait(15)
        common.clickById(Noxmobi.rewardbutton.show)
        common.wait(20)
        common.clickCenter()
        common.wait(2)
        #规避不同广告差异
        common.activateApp(Noxmobi.bundle_id.bundleid)
        common.swipeDown()
        common.clickById(Noxmobi.unityads.adclosename)

    def test_reward_nox_sdk_request(self):
        """nox_sdk_request广告请求打点"""
        reward = common.logBlockKeywordExist(Model.reward_nox_sdk_request, Model.firebaselog)
        assert reward

    def test_reward_nox_sdk_waterfall(self):
        reward = common.logBlockKeywordExist(Model.reward_nox_sdk_waterfall_request, Model.firebaselog)
        assert reward

    def test_reward_nox_sdk_show(self):
        reward = common.logBlockKeywordExist(Model.reward_nox_sdk_show, Model.firebaselog)
        assert reward

    def test_reward_nox_sdk_click(self):
        reward = common.logBlockKeywordExist(Model.reward_nox_sdk_click, Model.firebaselog)
        assert reward

    def test_reward_nox_sdk_show_failed(self):
        Noxmobisdk.checkFailedMsg()

    def teardown(self):
        pass

    def teardown_class(self):
        logging.info('这是结尾清除动作')
        common.terminateApp(Noxmobi.bundle_id.bundleid)
        # common.quit()
        common.logcatIosKill(self.pid)
        common.logcatIosKill(self.pid1)

