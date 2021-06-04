import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium import webdriver
from base_level.baseutil import BaseUtil
from excel.excelutil import ExcelUtil
import pytest
from page_level.page import LoginPage
class TestLogin(BaseUtil):
    @pytest.mark.parametrize("index,username,password",ExcelUtil().read_excel())
    def test_login(self,index,username,password):
        """ 退出 """
        lp = LoginPage(self.driver)
        if username==None:
            username=""
        if password==None:
            password=""
        lp.login(username,password)
        if index==1:
            # 断言
            assert lp.get_except_result()=='welcome'