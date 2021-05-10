import pytest

# 运行于测试方法的始末，即:运行一次测试函数会运行一次setup和teardown
class Test_ABC():
    def setup(self):
        print('\n---setup_method')

    def teardown(self):
        print('---teardown_method')
    def test_step(self):
        print('---step test1')
        assert 1
    def test_step2(self):
        print('---step test2')
        assert 1 > 2
    def test_step3(self):
        print('---step test3')
        assert 1
# 运行于测试方法的始末，即:运行一次测试函数会运行一次setup和teardown
class Test_ABClass():
    def setup_class(self):
        print('\n---setup_method')
    def teardown_class(self):
        print('---teardown_method')
    def test_step(self):
        print('---step test1')
        assert 1
    def test_step2(self):
        print('---step test2')
        assert 1 > 2
    def test_step3(self):
        print('---step test3')
        assert 1
if __name__ == '__main__':
    pytest.main('-s test_pytest.py')
