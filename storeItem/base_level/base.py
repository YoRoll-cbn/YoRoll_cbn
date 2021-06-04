from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        """
        页面加载
        """
        self.driver = driver

    def locator_element(self,loc):
        """
        定位元素//a[@title="删除"]/i
        """
        return self.driver.find_element(*loc)
    def locator_elements(self,loc):
        """
        定位多个元素
        """
        return self.driver.find_elements(*loc)

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
    def soloclicks(self,loc1,loc2,value):
        """
        封装后的elements的click()方法的solodelete
        """
        for i in range(1,value):
            self.locs=self.locator_elements(loc1)[i].click()
            self.locator_element(loc2).click()
            time.sleep(3)
    def clicks(self,loc,value):
        """
        封装后的elements的click()方法
        """
        self.locs=self.locator_elements(loc)
        for i in range(value):
            self.locs[i].click()

    def get_value(self,loc):
        """
        封装后的text()方法
        """
        return self.locator_element(loc).text
    def move_to(self,loc1,loc2):
        """
        封装后的move_to方法
        """
         # 第一步：实例化ActionChains
        ac=ActionChains(self.driver)
        # 第二步：定位要操作的元素
        ele1=self.locator_element(loc1)
        # 第三步：执行对应的操作
        ac.move_to_element(ele1)
        # 第四步，释放鼠标动作
        time.sleep(2)
        ac.perform()
        # 点击悬停出来的页面上的元素
        wait = WebDriverWait(self.driver, 10)
        ele2=self.locator_element(loc2)
        wait.until(EC.visibility_of_element_located(loc2))
        ele2.click()
    def get_attribute(self,loc,value):
        """
        封装后的get_attribute方法
        """
        return self.locator_element(loc).get_attribute(value)
    def function(self,loc1,loc2,value):
        """
        进入对应模块后点击对应的功能
        """
        #进入模块
        self.locator_element(loc1).click()
        self.locator_element(loc2).click()
        #进入框架
        self.driver.switch_to.frame(value)