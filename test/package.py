import os
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    #使用unittest默认的测试用例的加载器去发现test目录下以py结尾的所有的测试用例
    suite = unittest.defaultTestLoader.discover("./test","test*.py")
    #生成html报告文件
    file = open("./report/reports.html","wb")
    #s生成一个HTMLTestRunenr运行器对象（必须下载一个文件HTMLTestRunner.py，放到python的lin目录）
    runner = HTMLTestRunner(stream=file,title="自动化测试报告", description="报告详情如下：")
    #通过运行器去运行
    runner.run(suite)