from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#创建浏览器对象
driver = webdriver.Chrome()
#隐式等待5秒
driver.implicitly_wait(5)
#网易云登录自动化
driver.get("https://music.163.com/")
#最大化当前页面
driver.maximize_window()
#定位元素
#定位登录
driver.find_element(By.XPATH,"//a[text()='登录']").click()
#定位选择其他登录模式
driver.find_element(By.XPATH,"//a[text()='选择其他登录模式']").click()
#定位同意协议勾选框
driver.find_element(By.XPATH,"//input[@id='j-official-terms']").click()
#点击QQ登录
driver.find_element_by_partial_link_text("QQ登录").click()
# 获取当前所有标签页句柄
wins = driver.window_handles    # 返回的是一个列表，按照标签页打开的顺序
# 切换到第二个标签页
driver.switch_to.window(wins[1])
time.sleep(2)
#进入框架
driver.switch_to_frame(0)
#点击头像登录
driver.find_element_by_id("img_out_2356823260").click()
# driver.switch_to.window(wins[0])