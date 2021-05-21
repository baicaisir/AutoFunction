import subprocess
import re
import platform
from baseview import Baseview
from model import Model


class Commmon(Baseview):
    # 抓取iOS的log
    def logcatIos(self,logname='iphone.log'):
        '''
        :function:抓取iPhone的log
        :return:进程号
        '''
        # p = subprocess.Popen('idevice_id -l',shell=True)
        p = subprocess.Popen('idevicesyslog > %s '%logname,shell=True,cwd=Model.logdirpath,)
        return p.pid

    # 日志抓取完成，杀掉进程
    def logcatIosKill(self,pid):
        '''
        ：function：日志抓取结束杀掉进程
        :param pid: logcatIos返回的进程ID
        :return:
        '''
        if platform.system() == 'Windows':
            subprocess.call('taskkill /PID %s' % pid, shell=True)
        else:
            subprocess.call('kill %s'%pid,shell=True)
        return True

    # 从log中匹配关键字
    def logKeywordExist(self,pattern,filepath):
        '''
        ：function :按照每行匹配关键字
        :param pattern: 正则匹配规则
        :param filepath: log文件的路径
        :return: 返回去重升序后的匹配结果列表
        '''
        # if pattern1:
        #     subprocess.call('cat %s | grep %s > iphonelimit.log'%(filepath,pattern1),cwd=Model.logdirpath,shell=True)
        #     filepath = Model.logdirpath+'iphonelimit.log'
        wordlist = []
        with open(file=filepath,encoding='utf-8') as f:
            for i in f:
                wordlist += re.compile(pattern).findall(i)
        wordlist = list(set(wordlist))
        wordlist.sort()
        print(wordlist)
        # print(f'\033[0;32;47m{wordlist}\033[0m')
        return wordlist

        # 从log中匹配关键字
    def logBlockKeywordExist(self,pattern,filepath,blocksize = 1*1024*1024):
        '''
        ：function :按照数据块大小匹配关键字
        :param pattern: 正则匹配规则
        :param filepath: log文件的路径
        :return: 返回去重升序后的匹配结果列表
        '''
        wordlist = []
        with open(file=filepath,encoding='utf-8') as f:
            buffer = -1
            while buffer:
                buffer = f.read(blocksize)
                wordlist += re.compile(pattern).findall(buffer)
        wordlist = list(set(wordlist))
        wordlist.sort()
        # print(wordlist)
        # print(f'\033[0;32;47m{wordlist}\033[0m')
        return wordlist

    def keywordLogZip(self,loglist,keyword,i,start = 1):
        '''
        :function:生成pytest的断言参数
        :param loglist: 正则匹配出来的关键字列表
        :param keyword: 检测的关键字，eg：level 12345
        :param i: 等级的范围
        :param start: 默认从0开始匹配
        :return: 返回的是pytest需要的格式--[('kayak', True), ('civic', True), ('forest', False)]
        '''
        keywordlist = [(keyword + str(i)) for i in range(start,i)]
        testlist = list(zip([loglist] * len(keywordlist), keywordlist))
        return testlist

    def keywordListLogZip(self,loglist,keywordlist):
        '''
        :function:生成pytest的断言参数
        :param loglist: 正则匹配出来的关键字列表
        :param keywordlist: 检测的关键字列表
        :return: 返回的是pytest需要的格式--[('kayak', True), ('civic', True), ('forest', False)]
        '''
        testlist = list(zip([loglist] * len(keywordlist), keywordlist))
        return testlist

    @classmethod
    def getclass(self,pa,index):
        Baseview.getclasses(pa,index)
