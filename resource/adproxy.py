# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 19:39
# @Author  : 
# @File    : adproxy.py
# @Software: PyCharm

import json
import pymysql

from mitmproxy import http

ad_source, ad_type, system = "AdMob", 4, "ios"

def getdata(ad_source, ad_type, system):
    db = pymysql.connect("10.8.1.200", "qaplatform", "qaplatform", "qaplatform")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT config from sdk_network_info where ad_source='%s' and ad_type=%d and system='%s'" % (ad_source, int(ad_type), system))
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("数据格式%s" % data[0])
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
        print('全部数据为', data)
        print('替换数据为', addata)
        data['responseData']['noxmobiMediationConfig']['highRequestPool']['adRequestSettings'] = [addata]
        flow.response.text = json.dumps(data)
        print('相应数据为', flow.response.text)
