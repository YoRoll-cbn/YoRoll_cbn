from ddt import ddt, data, unpack
from selenium import webdriver
from baseutil import BaseUtil
from excelutil import ExcelUtil
from page import LoginPage

@ddt
class TestLogin(BaseUtil):
    @data(*ExcelUtil().read_excel())
    @unpack
    def test_login(self,index,username,password):
        """ 登录 """
        lp = LoginPage(self.driver)
        if username==None:
            username=""
        if password==None:
            password=""
        lp.login(username,password)
        if index==1:
            # 断言
            self.assertEqual(lp.get_except_result(),'welcome')