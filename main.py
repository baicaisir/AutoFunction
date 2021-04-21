from aw import common
import time
import pytest

def logcat():
    p = common.logcatIos()
    input('测试结束回车就可以了')
    common.logcatIosKill(p)

    # subprocess.call('pytest --pyargs scripts',shell=True)
filetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
print(filetime)
if __name__ == '__main__':
    # logcat()
    pytest.main(['-k test','scripts/test_pytest.py',f'--html=report/{filetime}/report.html'])