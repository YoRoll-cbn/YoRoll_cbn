from selenium import webdriver
from baseutil import BaseUtil
from excelutil import ExcelUtil
from page import LoginPage
import pytest

class TestLogin(BaseUtil):
    @pytest.mark.parametrize("index,username,password",ExcelUtil().read_excel())
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
            assert lp.get_except_result()=='welcome'