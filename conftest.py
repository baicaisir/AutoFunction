#coding:utf-8
from baseview import md
from model import Model
import logging
import pytest


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    logging.debug('截图名称为：%s' % report)
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail) or (report.passed and xfail):
            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace(".py", "")+".png"
            file_name = './report/assets/' + file_name
            logging.debug('截图完整路径为：%s' % file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:200px;height:400px;" ' \
                       'οnclick="window.open(this.src)" align="right"/></div>' % file_name.replace('report/', '')
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    md.get_screenshot_as_file(name)


# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#     return driver