import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium import webdriver
from base_level.baseutil import BaseUtil
from page_level.pagePwd import PwdPage
import pytest

class TestPwd(BaseUtil):
    @pytest.mark.parametrize("index,newpassword,surepassword",[(1,"123456","123456"),(2,"123456","1234567"),(3,"12345","12345"),(4,"","666666"),(5,"666666",""),(6,"12345678912345600","12345678912345600"),(7,"666666","666666")])
    def test_pwd(self,index,newpassword,surepassword):
        """ 修改密码 """
        pd=PwdPage(self.driver)
        pd.pwd(newpassword,surepassword)
        # 断言
        if index==1:
            assert pd.get_except_result()=='新密码与原密码相同，请重新输入！'
        if index==7:
            assert pd.get_except_result()=='修改密码成功'
