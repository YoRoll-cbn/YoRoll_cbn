import time
from selenium import webdriver


# 启动Chromedriver，并与Chromedriver开启会话
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()

# 获取当前标签页句柄
wins = driver.current_window_handle
print('当前标签页：', wins)

# 点击其中一个百度结果，出现一个新标签页
driver.find_element_by_xpath('//h3[@class="t c-gap-bottom-small"]//a').click()
time.sleep(2)

# 获取当前所有标签页句柄
wins = driver.window_handles    # 返回的是一个列表，按照标签页打开的顺序
print('所有标签页1：', wins)

# 切换到第一个标签页
driver.switch_to.window(wins[0])
time.sleep(2)

# 打开新的标签页
js = 'window.open("https://www.cnblogs.com/miki-peng/")'
driver.execute_script(js)
time.sleep(2)

# 再次获取当前所有标签页句柄
wins = driver.window_handles
print('所有标签页2：', wins)

# 关闭当前标签页
driver.close()

time.sleep(3)
driver.quit()  # 关闭浏览器，kill掉chromedriver进程
