**Q&A**

### Q1：UnicodeDecodeError: 'gbk' codec can't decode byte 0xb0 in position 35: illegal multibyte sequence

A1：pytest.ini文件编码问题，win设备默认以GBK编码执行导致编码错误，可以把ini文件替换成GBK格式，或者win设备默认编码格式修改为utf-8；
或者修改Python的默认执行编码方式：在Python安装目录下的Lib/site-packages目录中，新建一个sitecustomize.py文件（也可以建在其它地方，然后手工导入，建在这里，每次启动Python的时候设置将自动生效），内容如下： import _locale _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

### Q2:详细日志不显示？

A2:[pytest]配置
addopts = -v --html=report/reporttest.html
配置时加了-s参数，导致详细日志不显示