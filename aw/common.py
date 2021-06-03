# -*- coding: utf-8 -*-
import subprocess
import re
import platform
from baseview import md
from model import Model

def logcatIos(logname='iphone.log'):
    """
    :function:抓取iPhone的log
    :return:进程号
    """
    # p = subprocess.Popen('idevice_id -l', shell=True)
    p = subprocess.Popen('idevicesyslog > %s' %logname, shell=True, cwd=Model.logdirpath)
    return p.pid

# 日志抓取完成，杀掉进程
def logcatIosKill(pid):
    """
    ：function：日志抓取结束杀掉进程
    :param pid: logcatIos返回的进程ID
    :return:
    """
    if platform.system() == 'Windows':
        subprocess.call('taskkill /PID %s' %pid,  shell=True)
    else:
        subprocess.call('kill %s' %pid, shell=True)
    return True

# 从log中匹配关键字
def logKeywordExist(pattern, filepath):
    """
    ：function :按照每行匹配关键字
    :param pattern: 正则匹配规则
    :param filepath: log文件的路径
    :return: 返回去重升序后的匹配结果列表
    """
    # if pattern1:
    #     subprocess.call('cat %s | grep %s > iphonelimit.log'%(filepath, pattern1), cwd=Model.logdirpath, shell=True)
    #     filepath = Model.logdirpath+'iphonelimit.log'
    wordlist = []
    with open(file=filepath, encoding='utf-8') as f:
        for i in f:
            wordlist += re.compile(pattern).findall(i)
    wordlist = list(set(wordlist))
    wordlist.sort()
    print(wordlist)
    # print(f'\033[0;32;47m{wordlist}\033[0m')
    return wordlist

    # 从log中匹配关键字
def logBlockKeywordExist(pattern, filepath, blocksize=1*1024*1024):
    """
    ：function :按照数据块大小匹配关键字
    :param pattern: 正则匹配规则
    :param filepath: log文件的路径
    :param blocksize: 每次读取的内存大小
    :return: 返回去重升序后的匹配结果列表
    """
    wordlist = []
    with open(file=filepath, encoding='utf-8') as f:
        buffer = -1
        while buffer:
            buffer = f.read(blocksize)
            wordlist += re.compile(pattern).findall(buffer)
    wordlist = list(set(wordlist))
    wordlist.sort()
    # print(wordlist)
    # print(f'\033[0;32;47m{wordlist}\033[0m')
    return wordlist

def keywordLogZip(loglist, keyword, i, start=1):
    """
    :function:生成pytest的断言参数
    :param loglist: 正则匹配出来的关键字列表
    :param keyword: 检测的关键字，eg：level 12345
    :param i: 等级的范围
    :param start: 默认从0开始匹配
    :return: 返回的是pytest需要的格式--[('kayak',  True),  ('civic',  True),  ('forest',  False)]
    """
    keywordlist = [(keyword + str(i)) for i in range(start, i)]
    testlist = list(zip([loglist] * len(keywordlist),  keywordlist))
    return testlist

def keywordListLogZip(loglist, keywordlist):
    """
    :function:生成pytest的断言参数
    :param loglist: 正则匹配出来的关键字列表
    :param keywordlist: 检测的关键字列表
    :return: 返回的是pytest需要的格式--[('kayak',  True),  ('civic',  True),  ('forest',  False)]
    """
    testlist = list(zip([loglist] * len(keywordlist),  keywordlist))
    return testlist


def getClassProperty(classname, index) -> object:
    """
    :function:通过class获取对应位置的属性
    :param classname: 控件的class名称
    :param index: 控件的索引值
    :return: 返回控件属性
    """

    return md.getClasses(classname, index)

def getValueById(name):
    text = md.findByAccessibilityId(name).get_attribute('value')
    return text

def checkValue(value):
    """
    用来断言使用
    :param value:传入bool值
    :return:
    """
    assert value
def clickByAccessibilityId(idname):
    """
    通过name点击控件
    :param name:
    :return:
    """
    return md.findByAccessibilityId(idname).click()

def clickByXpath(xpath):
    """
    通过xpath点击控件
    :param name:
    :return:
    """
    return md.findByXpath(xpath).click()

def wait(t = 1):
    """
    执行等待
    :param t:默认是一秒钟
    :return:
    """
    return md.wait(t)

def goBack(n = 1):
    """
    返回键
    :param n: 点击次数
    :return:
    """
    for i in range(n):
        print('返回第%s次'%i)
        md.goBack()
        md.wait(1)

def clickByLocation(x,y):
    """
    通过页面坐标点击---ios
    :param x: x轴坐标
    :param y: y轴坐标
    :return:
    """
    md.tapByLocation(x,y)

def quit():
    """设备退出"""
    return md.quit()