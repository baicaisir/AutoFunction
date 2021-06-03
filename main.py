from aw import common
import time
import pytest
import subprocess


def logcat():
    p = common.logcatIos('firebase.log')
    input('测试结束回车就可以了')
    common.logcatIosKill(p)

    # subprocess.call('pytest --pyargs scripts',shell=True)

#获取当前时间年月日时分秒，用于创建输出日志存放的文件夹
filetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
print(filetime)

if __name__ == '__main__':
    # logcat()
    # subprocess.call('pytest  scripts/test_firebase.py',shell=True)

    #pytest-HTML报告
    # pytest.main(['-v','-k test', 'scripts/test_firebase.py', f'--html=report/{filetime}/report.html'])


    #allure-pytest报告--
    pytest.main(['--alluredir',f'./report/{filetime}/allure_raw','scripts/test_noxmobisdk.py'])
    subprocess.call(f'allure  serve ./report/{filetime}/allure_raw', shell=True)
