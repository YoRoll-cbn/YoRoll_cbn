import sys
sys.path.append(r"D:\python\GitHub\YoRoll_cbn\storeItem")
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_level.base import BasePage
from page_level.page import LoginPage
import time	
from selenium.webdriver.support.select import Select
class CumPage(BasePage):
    #页面的元素
    #定位基础管理
    basicManage=(By.XPATH,'//*[@id="menu-article"]/dt')
    #定位客户列表
    customer =(By.XPATH,'//a[text()="客户列表"]')
    #定位商品列表
    commodity =(By.XPATH,'//a[text()="商品列表"]')
    #定位刷新
    refresh=(By.XPATH,"/html/body/div[1]/nav/a")

    #定位添加
    addcustomer=(By.XPATH,'//*[@class="btn btn-primary radius"]')
    #定位输入
    name=(By.ID,"name")
    loginname=(By.ID,"loginname")
    pwd=(By.ID,"pwd")
    phone=(By.ID,"phone")
    bank=(By.ID,"bank")
    account=(By.ID,"account")
    zip=(By.ID,"zip")
    email=(By.ID,"email")
    address=(By.ID,"address")
    place=(By.ID,"place")
    desc=(By.ID,"desc")
    #定位提交
    submit=(By.XPATH,'//*[@type="submit"]')
    #定位成功信息
    allsuccess=(By.XPATH,'//*[contains(@id,"layui-layer")]/div')
    # #定位框架
    # frame3=(By.XPATH,'//*[@id="iframe_box"]/div[3]/iframe')

    #定位下拉框
    selectframe=(By.XPATH,'//*[@id="data-table-list_length"]/label/select')
    #定位搜索框
    search=(By.XPATH,'//input[@type="search"]')
    #定位搜索到的内容
    content=(By.CLASS_NAME,"getData-list")

    #定位单个删除
    deletesolo=(By.XPATH,'//a[@title="删除"]/i')
    #定位删除选择
    deleteselect=(By.XPATH,'//*[@id="data-table-list"]/tbody/tr/td[1]/input')
    #定位批量删除按钮
    deletebatch=(By.XPATH,'//a[@onclick="datadel()"]')
    #定位确定
    deletesure=(By.CLASS_NAME,"layui-layer-btn0")
    #定位删除成功
    #deletesuccess=(By.XPATH,'//*[contains(@id,"layui-layer")]/div')
    #定位排序
    sort=(By.XPATH,'//th[contains(text(),"编号")]')

    #定位选择文件
    file=(By.ID,'image')

    def F5(self):
        """
        刷新
        """
        #登录
        lp=LoginPage(self.driver)
        lp.login("666@163.com","123456")
        #刷新
        self.function(CumPage.basicManage,CumPage.customer, 1)
        self.click(CumPage.refresh)

    def add(self,name,loginname,pwd,phone,bank,account,zip,email,address):
        """
        添加客户
        """
        #登录
        lp=LoginPage(self.driver)
        lp.login("666@163.com","123456")
        #进入框架添加客户
        self.function(CumPage.basicManage,CumPage.customer, 1)
        self.click(CumPage.addcustomer)
        #切换回主框架
        self.driver.switch_to.default_content()
        #进入添加用户的框架
        self.driver.switch_to.frame(2)
        #添加内容
        self.send_keys(CumPage.name, name)
        self.send_keys(CumPage.loginname, loginname)
        self.send_keys(CumPage.pwd, pwd)
        self.send_keys(CumPage.phone, phone)
        self.send_keys(CumPage.bank, bank)
        self.send_keys(CumPage.account, account)
        self.send_keys(CumPage.zip, zip)
        self.send_keys(CumPage.email, email)
        self.send_keys(CumPage.address, address)
        self.click(CumPage.submit)
        time.sleep(2)
        #刷新
        self.click(CumPage.refresh)
        #切换回主框架
        self.driver.switch_to.default_content()
        #添加成功 
        element_existance = True
        try:
            global addsuccessValue
            # 尝试寻找元素，如若没有找到则会抛出异常
            element = self.locator_element(CumPage.allsuccess)
        except:
            element_existance = False
        if element_existance:
            addsuccessValue =self.get_attribute(CumPage.allsuccess,'innerText')
    #断言
    def get_except_result1(self):
        return addsuccessValue
        
    
    def Select(self,value1,value2):
        """
        查找内容
        """
        #登录
        lp=LoginPage(self.driver)
        lp.login("666@163.com","123456")
        #进入框架查找
        self.function(CumPage.basicManage,CumPage.customer, 1)
        #选择下拉框
        sel=Select(self.locator_element(CumPage.selectframe))
        sel.select_by_value(value1)
        #搜索
        self.send_keys(CumPage.search, value2)
   #断言
    def get_except_result2(self):
        return self.get_value(CumPage.content)

    def delete(self,value1,value2):
        """
        删除
        """
        #登录
        lp=LoginPage(self.driver)
        lp.login("666@163.com","123456")
        #进入框架
        self.function(CumPage.basicManage,CumPage.customer, 1)
        #刷新
        self.click(CumPage.refresh)
        time.sleep(1)
        #排序
        self.click(CumPage.sort)
        self.click(CumPage.sort)
        #单个删除
        self.soloclicks(CumPage.deletesolo,CumPage.deletesure,value1)

        # global deleteSoloSuccess
        # element_existance = True
        # try:
        #     # 尝试寻找元素，如若没有找到则会抛出异常
        #     element = self.locator_element(CumPage.allsuccess)
        # except:
        #     element_existance = False
        # #if element_existance:
        # deleteSoloSuccess =self.get_attribute(CumPage.allsuccess,'innerText')

        #多个删除
        self.clicks(CumPage.deleteselect,value2)
        self.click(CumPage.deletebatch)
        self.click(CumPage.deletesure)

    #     global deleteBatchSuccess
    #     deleteBatchSuccess =self.get_attribute(CumPage.allsuccess,'innerText')
    #  #断言
    # def get_except_result3(self):
    #     return deleteSoloSuccess
    # def get_except_result4(self):
    #     return deleteBatchSuccess
    def pageswitch(self):
        pass
    def fileselect(self,value1,value2,value3,value4):
         #登录
        lp=LoginPage(self.driver)
        lp.login("666@163.com","123456")
        #进入框架添加客户
        self.function(CumPage.basicManage,CumPage.commodity, 1)
        self.click(CumPage.addcustomer)
        #切换回主框架
        self.driver.switch_to.default_content()
        #进入添加用户的框架
        self.driver.switch_to.frame(2)
        self.send_keys(CumPage.file,value1)
        self.send_keys(CumPage.name, value2)
        self.send_keys(CumPage.place,value3)
        self.send_keys(CumPage.desc, value4)
        self.click(CumPage.submit)

