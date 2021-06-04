import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium import webdriver
from base_level.baseutil import BaseUtil
from excel.excelutil import ExcelUtil
from page_level.pageExit import ExitPage
import pytest

class Testexit(BaseUtil):
    def test_exit(self):
        """ 退出 """
        et=ExitPage(self.driver)
        et.exit()

        # 断言
        assert et.get_except_result()=='loginWraper'
