# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:33
# @Author  : 
# @File    : test_firebase.py
# @Software: PyCharm

from aw import common
from model import Model
import logging


class Testfirebase:
    """ nox_sdk_waterfall 瀑布流请求打点  """
    def setup(self):
        logging.info('这是一个调试脚本')

    def test_banner_nox_sdk_waterfall(self):
        logging.info('cehsi ')
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_waterfall_request, Model.firebaselog)
        assert banner

    def test_int_nox_sdk_waterfall(self):
        Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_waterfall_request, Model.firebaselog)
        assert Interstitial != []

    def test_reward_nox_sdk_waterfall(self):
        Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_waterfall_request, Model.firebaselog)
        assert  Reward != []

    '''nox_sdk_show 广告展示打点'''
    def test_banner_nox_sdk_show(self):
        banner = common.logBlockKeywordExist(Model.banner_nox_sdk_show, Model.firebaselog)
        assert banner != []

    def test_int_nox_sdk_show(self):
        Interstitial = common.logBlockKeywordExist(Model.int_nox_sdk_show, Model.firebaselog)
        assert Interstitial != []

    def teardown(self):
        # common.quit()
        pass
    #
    # def test_reward_nox_sdk_show(self):
    #     Reward = common.logBlockKeywordExist(Model.reward_nox_sdk_show, Model.firebaselog)
    #     assert  Reward != []
    #
    # '''nox_sdk_request广告请求打点'''
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
    #     assert  Reward != []
    #
    #
    # '''nox_sdk_click  点击跳转打点'''
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
    #     assert  Reward != []
    #
    # '''三方mediation打点'''
    # '''请求配置打点'''
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
    # def test_third_mediation_banner_auto_refresh(self):
    #     banner = common.logBlockKeywordExist(Model.third_mediation_banner_auto_refresh, Model.firebaselog)
    #     assert banner != []
