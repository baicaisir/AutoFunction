# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_noxmobisdk.py
# @Software: PyCharm

import logging
from aw import common
from model import Noxmobi


class Testnoxmobi:

    """ setup  """
    def test_ad_show(self):
        common.setWinProxy()
        self.pid = common.openMitmweb()
        self.pid1 = common.logcatIos('firebase.log')
        logging.info('启动NoxmobiDemo')
        common.activate_app(Noxmobi.bundle_id.ID)
        common.wait(1)
        common.clickByAccessibilityId(Noxmobi.settingbutton.id)
        common.wait(5)
        # common.clickByXpath(Noxmobi.settingbutton.xpath)
        logging.info('点击控件%s'%Noxmobi.firebasebutton.name)
        common.clickById(Noxmobi.firebasebutton.name,index=1)
        common.wait(5)
        input('dengyidei')
        # common.quit()
        common.goBack(1)
        common.clickById(Noxmobi.interbutton.id)
        common.wait(1)
        common.clickById(Noxmobi.interbutton.init)
        common.wait(1)
        common.clickById(Noxmobi.interbutton.show)
        text = common.getValueById('Test mode')
        print(text, '===========')
        common.checkValue(text == 'Test mode')
        common.wait(5)
        common.clickCenter()
        common.wait(5)
        a = common.checkIdIsExist('URL')
        print(a)
        common.checkValue(a)

        # 通过坐标点击返回广告展示页
        common.clickByLocation(22, 22)

        # 广告关闭按钮位置
        logging.info('断言之后接着执行')
        common.wait(5)
        common.clickByLocation(20, 60)
        common.goBack(2)
        common.quit()
        common.logcatIosKill(self.pid)
        common.logcatIosKill(self.pid1)
        common.checkValue(text == 'Test mode')


    '''  nox_sdk_waterfall 瀑布流请求打点  '''

    # def test_banner_nox_sdk_waterfall(self):
    #     banner = common.logBlockKeywordExist(Model.banner_nox_sdk_waterfall_request, Model.firebaselog)
    #     common.checkValue(banner != [])
    #
    # def test_int_nox_sdk_waterfall(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_waterfall_request, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_nox_sdk_waterfall(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_waterfall_request, Model.firebaselog)
    #     assert Reward != []
    #
    # '''nox_sdk_show 广告展示打点'''
    #
    # def test_banner_nox_sdk_show(self):
    #     banner = common.logBlockKeywordExist(Model.banner_nox_sdk_show, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_nox_sdk_show(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_show, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_nox_sdk_show(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_show, Model.firebaselog)
    #     assert Reward != []
    #
    # '''nox_sdk_request广告请求打点'''
    #
    # def test_banner_nox_sdk_request(self):
    #     banner = common.logBlockKeywordExist(Model.banner_nox_sdk_request, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_nox_sdk_request(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_request, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_nox_sdk_request(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_request, Model.firebaselog)
    #     assert Reward != []
    #
    # '''nox_sdk_click  点击跳转打点'''
    #
    # def test_banner_nox_sdk_click(self):
    #     banner = common.logBlockKeywordExist(Model.banner_nox_sdk_click, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_nox_sdk_click(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_click, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_nox_sdk_click(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_click, Model.firebaselog)
    #     assert Reward != []
    #
    # '''三方mediation打点'''
    # '''请求配置打点'''
    #
    # def test_banner_nox_sdk_request_config(self):
    #     banner = common.logBlockKeywordExist(Model.banner_nox_sdk_request_config, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_nox_sdk_request_config(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_request_config, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_nox_sdk_request_config(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_request_config, Model.firebaselog)
    #     assert Reward != []
    #
    # '''sdk发起的一次广告请求'''
    #
    # def test_banner_third_mediation_request(self):
    #     banner = common.logBlockKeywordExist(Model.banner_third_mediation_request, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_third_mediation_request(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_third_mediation_request, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_third_mediation_request(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_third_mediation_request, Model.firebaselog)
    #     assert Reward != []
    #
    # '''广告展示'''
    #
    # def test_banner_third_mediation_show(self):
    #     banner = common.logBlockKeywordExist(Model.banner_third_mediation_show, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_third_mediation_showg(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_third_mediation_show, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_third_mediation_show(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_third_mediation_show, Model.firebaselog)
    #     assert Reward != []
    #
    # '''广告点击'''
    #
    # def test_banner_third_mediation_click(self):
    #     banner = common.logBlockKeywordExist(Model.banner_third_mediation_click, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_third_mediation_click(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_third_mediation_click, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_third_mediation_click(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_third_mediation_click, Model.firebaselog)
    #     assert Reward != []
    #
    # '''广告关闭'''
    #
    # def test_banner_third_mediation_close(self):
    #     banner = common.logBlockKeywordExist(Model.banner_third_mediation_close, Model.firebaselog)
    #     assert banner != []
    #
    # def test_int_third_mediation_close(self):
    #     Interstitial = common.logBlockKeywordExist(Model.int_third_mediation_close, Model.firebaselog)
    #     assert Interstitial != []
    #
    # def test_reward_third_mediation_close(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_third_mediation_close, Model.firebaselog)
    #     assert Reward != []
    #
    # '''banner自动刷新打点'''
    #
    # def test_third_mediation_banner_auto_refresh(self):
    #     banner = common.logBlockKeywordExist(Model.third_mediation_banner_auto_refresh, Model.firebaselog)
    #     assert banner != []
