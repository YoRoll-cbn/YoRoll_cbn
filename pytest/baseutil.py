import time
from selenium import webdriver

class BaseUtil:

    def setup(self):
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        #隐式等待
        self.driver.implicitly_wait(5)
        # 加载网页
        self.driver.get("http://storeweb.bithachi.cn/admin/Login/login.html")
        #最大化当前网页
        self.driver.maximize_window()
    
    def teardown(self):
        pass