from selenium import webdriver
import time
class BasePage:
    def __init__(self,driver):
        """
        页面加载
        """
        self.driver = driver

    def locator_element(self,loc):
        """
        定位元素
        """
        return self.driver.find_element(*loc)

    def send_keys(self,loc,value):
        """
        封装后的send_keys()方法
        """
        self.locator_element(loc).send_keys(value)

    def click(self,loc):
        """
        封装后的click()方法
        """
        self.locator_element(loc).click()
    
    def get_value(self,loc):
        """
        封装后的text()方法
        """
        return self.locator_element(loc).text