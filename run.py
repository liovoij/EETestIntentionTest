import pytest
import os

if __name__ == '__main__':
    # 生成 Allure 报告需要的数据存在 ./TestReport/temp 目录
    pytest.main(['-s', '--alluredir', './TestReport/temp', './TestCase/intention_test.py'])
    # 生成测试报告
    os.system('allure generate ./TestReport/temp -o ./TestReport/report --clean')
