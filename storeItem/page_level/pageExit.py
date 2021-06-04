import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_level.base import BasePage
from page_level.page import LoginPage

class ExitPage(BasePage):

    #页面的元素
    #定位超级管理员
    supervisor = (By.XPATH,'//*[@id="Hui-userbar"]/ul/li[2]/a')
    #定位退出
    exitButton =(By.LINK_TEXT,'退出')
    #定位登录页面
    login=(By().CLASS_NAME,'loginWraper')
    #页面的动作
    def exit(self):
       #登录
       lp=LoginPage(self.driver)
       lp.login("666@163.com","123456")
       #选择退出
       self.move_to(ExitPage.supervisor,ExitPage.exitButton)

    #断言
    def get_except_result(self):
        return self.get_attribute(ExitPage.login,"class")