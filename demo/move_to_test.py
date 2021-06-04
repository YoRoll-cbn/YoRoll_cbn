import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动Chromedriver，并与Chromedriver开启会话
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

# 第一步：实例化ActionChains
ac = ActionChains(driver)
# 第二步：定位要操作的元素
ele = driver.find_element_by_xpath('//span[@id="s-usersetting-top"]')
# 第三步：执行对应的操作
ac.move_to_element(ele)		# 悬浮操作
# 第四步，释放鼠标动作
ac.perform()

# 点击悬停出来的页面上的元素
wait = WebDriverWait(driver, 10)
loc = (By.XPATH, '//a[@class="setpref"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(2)
driver.quit()