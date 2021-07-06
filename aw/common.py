# -*- coding: utf-8 -*-
import logging
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
    p = subprocess.Popen('idevicesyslog > %s' % logname, shell=True, cwd=Model.logdirpath)
    return p.pid

# 日志抓取完成，杀掉进程
def logcatIosKill(pid):
    """
    ：function：日志抓取结束杀掉进程
    :param pid: logcatIos返回的进程ID
    :return:
    """
    if platform.system() == 'Windows':
        subprocess.call('taskkill /PID %s' % pid, shell=True)
    else:
        subprocess.call('kill %s' % pid, shell=True)
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


def logBlockKeywordExist(pattern, filepath, blocksize=1 * 1024 * 1024):
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
    testlist = list(zip([loglist] * len(keywordlist), keywordlist))
    return testlist


def keywordListLogZip(loglist, keywordlist):
    """
    :function:生成pytest的断言参数
    :param loglist: 正则匹配出来的关键字列表
    :param keywordlist: 检测的关键字列表
    :return: 返回的是pytest需要的格式--[('kayak',  True),  ('civic',  True),  ('forest',  False)]
    """
    testlist = list(zip([loglist] * len(keywordlist), keywordlist))
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


def clickById(idname, index):
    """
    :param idname:
    :param index:
    :return:
    """
    return md.clickByid(idname, index)


def checkValue(value):
    """
    用来断言使用
    :param value:传入bool值
    :return:
    """
    assert value


def clickById(name):
    """
    通过name点击控件
    :param name:
    :return:
    """
    return md.findByAccessibilityId(name).click()


def clickByIds(name, index=0):
    """
    通过name点击控件
    :param name:
    :param index:
    :return:
    """
    return md.findElementsByAccessibilityId(name)[index].click()

def click_by_class_name(classname, index=0):
    """
    通过classname点击控件
    :param classname:
    :param index:按照列表索引值格式，从0开始
    :return:
    """
    return md.find_elements_by_class_name(classname)[index].click()


def clickByXpath(xpath):
    """
    通过xpath点击控件
    :param xpath:
    :return:
    """
    return md.findByXpath(xpath).click()


def wait(t=1):
    """
    执行等待
    :param t:默认是一秒钟
    :return:
    """
    return md.wait(t)


def goBack(n=1):
    """
    返回键
    :param n: 点击次数
    :return:
    """
    for i in range(n):
        print('返回第%s次' % i)
        md.goBack()
        md.wait(1)


def clickByLocation(x, y):
    """
    通过页面坐标点击---ios
    :param x: x轴坐标
    :param y: y轴坐标
    :return:
    """
    md.tapByLocation(x, y)


def clickCenter():
    """点击屏幕中心位置"""
    md.clickCenter()

def terminateApp(id):
    """
    杀掉应用进程
    :param id: iOS：Bundle ID ；Android：package
    :return:
    """
    md.terminateApp(id)

def activateApp(id):
    """
    启动应用
    :param id: iOS：Bundle ID ；Android：package
    :return:
    """
    md.activateApp(id)

def backgroudApp(time):
    """
    回到回桌面一段时间后返回
    :param time:
    :return:
    """
    md.backgroudApp(time)

def quit():
    """设备退出"""
    return md.quit()


def checkIdIsExist(idname):
    """判断是否存在某个ID/name"""
    if md.findElementsByAccessibilityId(idname):
        return True
    else:
        return False

def changeFileContent(pattern, repl, filepath):
    """
    利用正则替换文件内容
    :param pattern:正则规则
    :param repl:替换的字符串
    :param filepath:文件路径
    :return:
    """
    with open(file=filepath, encoding='utf-8') as f:
        buffer = f.read()
        pa1 = re.compile(pattern).findall(buffer)[0]
        filecontent = re.sub(pa1, repl, buffer)
        print(filecontent)

    with open(filepath, mode='w+', encoding='utf-8') as f:
        f.write(filecontent)

def setWinProxy(host='127.0.0.1', post=8888, clear=False):
    """
    win设置代理/清除代理
    :param host: 代理ip
    :param post: 代理端口
    :param clear: 是否清除代理
    :return:
    """
    if clear:
        subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f && reg add "HKCU\Softwae \Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "" /f', shell=True)
        print('清除系统代理成功')
    else:
        subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f && reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "%s:%s" /f'% (host, post), shell=True)
        print('设置代理成功')

def openMitmweb(filepath=Model.logdirpath.proxypath):
    """
     启动mitmweb功能
    :param filepath: 脚本路径
    :return: 进程pid
    """
    p = subprocess.Popen('mitmweb -p 8888 -s %s'%filepath, shell=True, cwd=Model.logdirpath)
    logging.info('mitmweb进程ID%s'%p.pid)
    return p.pid