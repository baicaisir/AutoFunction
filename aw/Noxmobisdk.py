# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 15:47
# @Author  : 
# @File    : Noxmobisdk.py
# @Software: PyCharm


from aw import common
import logging
from model import Noxmobi
from model import Model


def openFirebaseButton():
    """
    打开Noxmobi——ios的firebase开关
    :return:
    """
    common.activateApp(Noxmobi.bundle_id.bundleid)
    common.wait(1)
    common.clickById(Noxmobi.settingbutton.id)
    common.wait(5)
    logging.info('点击控件%s' % Noxmobi.firebasebutton.name)
    common.clickByIds(Noxmobi.firebasebutton.name, index=1)


def backFromAppBar():
    """
    ios设备通过顶部导航栏返回app页面
    :return:
    """
    common.clickByLocation(36, 36)

def checkFailedMsg():
    configerrormsg = common.logBlockKeywordExist(Model.nox_sdk_request_config_failed, Model.firebaselog)
    waterfallerrormsg = common.logBlockKeywordExist(Model.nox_sdk_waterfall_request_failed, Model.firebaselog)
    if 'Null' in configerrormsg[-1]:
        logging.info('nox_sdk_request_config没有获取到失败信息')

        if 'Null' in waterfallerrormsg[-1]:
            logging.info('nox_sdk_waterfall_request没有获取到失败信息')
            errormsg = unicodeToChina(waterfallerrormsg[-1])
            logging.info(errormsg)
            assert 1
        else:
            logging.error('nox_sdk_waterfall_request失败原因如下：')
            errormsg = unicodeToChina(waterfallerrormsg[-1])
            logging.info(errormsg)
            assert 0
    else:
        logging.error('nox_sdk_request_config失败原因如下：')
        errormsg = unicodeToChina(configerrormsg[-1])
        logging.info(errormsg)
        assert 0


def unicodeToChina(unicodestr):
    """
    Unicode 字符转中文，
    ：主要用于转化win报错信息输出为Unicode类型
    :param unicodestr:unicode类型字符串，log输出类型
    :return:
    """
    chinastr = unicodestr.lower().replace('134','').encode('utf-8').decode('unicode_escape')
    return chinastr