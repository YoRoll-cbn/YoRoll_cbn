import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_level.base import BasePage
from page_level.page import LoginPage
import time	
class PwdPage(BasePage):

    #页面的元素
    #定位超级管理员
    supervisor = (By.XPATH,"//*[text()='超级管理员 ']")
    #定位修改密码
    pwdButton =(By.LINK_TEXT,'修改密码')
    #定位新密码输入
    newpwd=(By.ID,'newpassword')
    #定位确认密码
    insurepwd=(By.ID,'newpassword2')
    #定位确定
    sure=(By.XPATH,"//input[contains(@value,'提交')]")
    #定位返回
    goback=(By.XPATH,"//input[contains(@value,'返回')]")
    #定位修改密码成功
    success=(By.XPATH,'//*[contains(@id,"layui-layer")]/div')
    
    #页面的动作
    def pwd(self,newpassword,surepassword):
       #登录
       lp=LoginPage(self.driver)
       lp.login("666@163.com","123456")
       #选择修改密码
       self.move_to(PwdPage.supervisor,PwdPage.pwdButton)
       #输入密码提交并返回
       self.send_keys(PwdPage.newpwd,newpassword)
       self.send_keys(PwdPage.insurepwd,surepassword)
       time.sleep(1)
       self.click(PwdPage.sure)
       global successValue
       element_existance = True
       try:
            # 尝试寻找元素，如若没有找到则会抛出异常
            element = self.locator_element(PwdPage.success)
       except:
            element_existance = False
       if element_existance:
          successValue=self.get_attribute(PwdPage.success,'innerText')
       time.sleep(2)
       self.click(PwdPage.goback)
   #断言
    def get_except_result(self):
       return successValue