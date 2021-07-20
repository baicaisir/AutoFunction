# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 15:47
# @Author  : 
# @File    : Noxmobisdk.py
# @Software: PyCharm



from aw import common
import logging
from model import Noxmobi
# from model import Model


def openFirebaseButton():
    common.activateApp(Noxmobi.bundle_id.ID)
    common.wait(1)
    common.clickById(Noxmobi.settingbutton.id)
    common.wait(5)
    logging.info('点击控件%s' % Noxmobi.firebasebutton.name)
    common.clickByIds(Noxmobi.firebasebutton.name, index=1)