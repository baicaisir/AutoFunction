# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 19:39
# @Author  : 
# @File    : adproxy.py
# @Software: PyCharm

import json
import pymysql

from mitmproxy import http


ad_source, ad_type, system = "Vungle", 3, "ios"

def getdata(ad_source, ad_type, system):
    db = pymysql.connect("10.8.1.200", "qaplatform", "qaplatform", "qaplatform")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT config from sdk_network_info where ad_source='%s' and ad_type=%d and system='%s'" % (ad_source, int(ad_type), system))
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # print("数据格式%s" % data[0])
    # 关闭数据库连接
    db.close()
    return data[0]


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    print(flow.request.pretty_url, '=================================')
    addata = getdata(ad_source, ad_type, system)
    addata = json.loads(addata)

    if "ssp-3-9f58.trnox.com/ssp/ws/sdk/mediation/ad/config/info/" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # print('全部数据为', data)
        # print('替换数据为', addata)
        if data['responseData'].get('noxmobiMediationConfig'):
            data['responseData']['noxmobiMediationConfig']['highRequestPool']['adRequestSettings'] = [addata]
        else:
            data = {"errNum":0,"noxmobidebuglog":"yes","message":"SUCCESS","responseData":{"adNetWorkUnits":[],"adType":3,"appkey":"00ccca6049b44b1a9ef9067b9b7659f1","bannerRefreshFrequency":120,"bucketIds":" - 1, -1, 3","configSessionId":"5ec80de16d3c4bd398a9150fdede06e4","isNoxmobi":1,"noxmobiMediationConfig":{"clickLimit":[{"adSource":"AdMob, Facebook, GoogleDFP","limit":10}],"highRequestPool":{"adRequestPoolSettings":[{"cacheSize":1,"concurrentNum":1,"requestCountMax":999,"requestCountMin":1}],"adRequestSettings":[{"adSource":"AdMob","adUnitId":"ca-app-pub-3940256099942544/1712485313","adUnitType":3,"apiKey":"pub-7733038146743471","loopTime":1,"networkAppId":"ca-app-pub-7733038146743471~9845555226","timeout":60}],"cacheSize":1,"concurrentNum":1},"lowRequestPool":{"adRequestPoolSettings":[{"cacheSize":1,"concurrentNum":1,"requestCountMax":999,"requestCountMin":1}],"adRequestSettings":[],"cacheSize":1,"concurrentNum":1},"maxConcurrent":2,"policyCode":"2.0.0","requestInterval":30,"requestTiming":1,"retryInterval":30,"retryTime":1},"placementId":"110558d4350c45bca85893791dd2dd58","placementName":"qa_mock_config","token":"57e169b7503af9c9f99188488388d4bc"}}
            data['responseData']['noxmobiMediationConfig']['highRequestPool']['adRequestSettings'] = [addata]
        flow.response.text = json.dumps(data)
        # print('相应数据为', flow.response.text)
