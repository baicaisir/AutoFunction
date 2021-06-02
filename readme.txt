工程整体结构：
report：存放执行日志
aw(Action Word)：存放功能函数
model：常量定义，便于维护
resource：存放一些生成的log，或者需要使用的资源文件，例如apk
scripts：存放脚本


脚本执行命令：
pytest script --html=report/report.html

[--html=report/report.html]  日志

pytest.ini文件最好用UTF-8编码方式创建
MAC的编码方式不同，新建文件可能会导致程序执行编码错误

重试运行cases
某些情况来说可以通过重试运行cases的方式来解决
pytest test_se.py --reruns NUM

相关参数：
（1）‘-s’：关闭捕捉，输出打印信息。
（2）‘-v’:用于增加测试用例的详细信息。
（3）‘-k’ ：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行XX.py中包含add的测试用例。
（4）‘q’:减少测试的运行冗长。
（5）‘-x’:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
（6）‘-m’： 使用-m对用例进行标记，用例需注释@pytest.mark.xxx,将xxx作为参数传入
    使用-m "mark1 and mark2"可以同时选中带有这两个标记的所有测试用例。
    使用-m "mark1 and not mark2"选中带哟与mark1的测试用例，而过滤掉带有mark2的测试用例
    使用-m "mark1 or mark2"则选中带有mark1或者mark2的所有测试用例 """

allure格式报告
#执行以下命令会输出一份测试报告的原始文件
pytest —alluredir ./report/allure_raw
#执行一下命令可以将报告用HTML格式打开
allure serve report/allure_raw

mac通过.app安装应用
xcrun simctl install booted NoxmibiDemo.app