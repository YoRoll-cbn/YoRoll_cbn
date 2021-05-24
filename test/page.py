
from selenium.webdriver.common.by import By
from selenium import webdriver
from base import BasePage

class LoginPage(BasePage):

    #页面的元素
    #定位用户名输入
    username_loc = (By.ID,"adminName")
    #定位密码输入
    password_loc = (By.ID,"password")
    #定位登录按钮
    login_button = (By.XPATH,"//input[@class='btn btn-success radius size-L']")
    #定位welcome
    welcome= (By.XPATH,"//li[text()='welcome']")
    #页面的动作
    def login(self,username,password):
        self.send_keys(LoginPage.username_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.login_button)

    #断言
    def get_except_result(self):
        return self.get_value(LoginPage.welcome)