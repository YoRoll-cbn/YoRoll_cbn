import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium import webdriver
from base_level.baseutil import BaseUtil
import pytest
from page_level.pageCustomer import CumPage
from excel.excelutil2 import ExcelUtil2
class TestCum(BaseUtil):
    def test_cumF5(self):
        """客户列表刷新"""
        rf=CumPage(self.driver)
        rf.F5()
    
    @pytest.mark.parametrize("index,name,loginname,pwd,phone,bank,account,zip,email,address",ExcelUtil2().read_excel())
    def test_cumAdd(self,index,name,loginname,pwd,phone,bank,account,zip,email,address):
        """
        添加客户
        """
        ac=CumPage(self.driver)
        if index==6:
            name=loginname=pwd=phone=bank=account=zip=email=address=""
        ac.add(name,loginname,pwd,phone,bank,account,zip,email,address)
        # 断言
        if index<=4:
            assert ac.get_except_result1()=='添加成功！'
        # if index==7:
        #     assert ac.get_except_result()=='用户名已注册，请重新输入！'
    @pytest.mark.parametrize("value1,value2",[("25","YoRoll"),("50","zyq"),("100","wyx")])
    def test_cumSelect(self,value1,value2):
        """
        搜索内容
        """
        cs=CumPage(self.driver)
        cs.Select(value1, value2)
        #断言
        assert value2 in cs.get_except_result2()

    @pytest.mark.parametrize("index,value1,value2",[(1,2,0),(2,0,2),(3,2,2)])
    def test_delete(self,index,value1,value2):
        cd=CumPage(self.driver)
        cd.delete(value1,value2)
        # #断言
        # if index==1:
        #     assert cd.get_except_result3()=="删除成功"
        #     assert cd.get_except_result4()=="网络错误！"
        # if index ==2:
        #     assert cd.get_except_result3()=="删除成功"
        # else:
        #     assert cd.get_except_result3()=="删除成功"
        #     assert cd.get_except_result4()=="删除成功"
    def test_file(self):
        fs=CumPage(self.driver)
        fs.fileselect("D:\picture\林彦俊.jpg","YoRoll-cbn", "重庆", "wxywoxiangnile")