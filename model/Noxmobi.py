# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 11:05 上午
# @Author  : 
# @File    : Noxmobi.py
# @Software: PyCharm

class Noxmobi:
    class closebutton(object):
        id = 'Close Advertisement'

    class settingbutton(object):
        id = '设置页'
        xpath = '//XCUIElementTypeStaticText[@name="设置页"]'

    class interbutton(object):
        id = 'Interstital示例'
        init = 'Init + SetDelegate'
        show = 'Show'
        testmode = 'Test mode'

    class bannerbutton(object):
        id = 'Banner示例'
        init = 'Init'
        show = 'Show'
        testmode = 'Test mode'

    class rewardbutton(object):
        id = 'RewardVideo示例'
        init = 'Init + SetDelegate'
        show = 'Show'
        testmode = 'Test mode'

    class testmodebutton(object):
        name = 'Test Mode'
        xpath = '//XCUIElementTypeSwitch[@name="Test Mode"]ß'

    class firebasebutton(object):
        name = 'Firebase'
        xpath = r'//XCUIElementTypeSwitch[@name="Firebase"]'

    class rcbutton(object):
        name = 'RC 初始化'
        xpath = '//XCUIElementTypeSwitch[@name="RC 初始化"]'

    class bundle_id(object):
        bundleid = 'com.noxgroup.talentedmusician'

    class applovin(object):
        adclickname = 'App Lovin Advertisement'
        adclosename = 'Close Advertisement'

    class facebook(object):
        adclickname = 'icon clickable area'

    class gdtmob(object):
        adclickname = 'webView_id'
        adclosename = 'closeButton_id'
        downloadButtonname = 'downloadButton_id'

    class googledfp(object):
        # adclickname = 'webView_id'
        adclosename = 'Close Advertisement'
        # downloadButtonname = 'downloadButton_id'

    class bytedance(object):
        # adclickname = 'webView_id'
        adclosename = 'endcard_close'
        adrewardclosename = 'landingpage_close'
        # downloadButtonname = 'downloadButton_id'

    class ironsource(object):
        downloadButtonname = 'DOWNLOAD NOW'

    class mopub(object):
        adclosename = '完成'
        adrewardclosename = 'Close ad'
        adclickname = 'Tap to test this ad.'

    class unityads(object):
        adclosename = 'Close'
        adclickname = '免费下载'

    class vungle(object):
        adclosename = 'Close'
        adclickname = 'banner'
        vunglename = 'Vungle'

    class startapp(object):
        adclickname = 'StartApp'

    class kuaishou(object):
        adclickname = '广告'
