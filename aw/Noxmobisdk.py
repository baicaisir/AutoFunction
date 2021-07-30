# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 15:47
# @Author  : 
# @File    : Noxmobisdk.py
# @Software: PyCharm


from aw import common
import logging
from model import Noxmobi


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
