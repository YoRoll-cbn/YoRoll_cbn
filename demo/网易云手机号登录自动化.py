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
#定位选择手机号登录按钮
driver.find_element(By.XPATH,'//a[@class="u-btn2 u-btn2-2"]').click()
#定位输入账号
driver.find_element(By.XPATH,"//input[@id='p']").send_keys("18163147707")
#定位输入密码
driver.find_element(By.XPATH,"//input[@id='pw']").send_keys("hcy90207")
#定位登录按钮
driver.find_element(By.XPATH,"//a[@class='j-primary u-btn2 u-btn2-2']").click()
#停留，保持在页面
os.system('pause')
#退出网页
driver.close()