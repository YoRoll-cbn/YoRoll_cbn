import os
import pytest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    #-vs表示打印结果
    #pytest.main('-vs')
     #第一步：生成json格式临时文件，--clean-alluredir表示每执行一次把temp目录先清除
    pytest.main(['-vs',r'D:\python\GitHub\YoRoll_cbn\StoreItem\testcase','--alluredir','./temp','--clean-alluredir'])
    #第二步：根据json格式临时文件生成allure报告
    os.system("allure generate ./pytest/temp -o ./reports --clean")