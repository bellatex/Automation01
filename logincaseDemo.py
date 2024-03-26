#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#启动浏览器
driver = webdriver.Chrome()
#打开url
driver.get("https://mail.sina.com.cn/register/regmail.php")
time.sleep(3)
#test : 判段打开页面是否正确  title_Contains
#EC.title_is 需要完全一样  EC.title_contains 部分or全部一样
print(EC.title_contains("注册"))
#查 传入元素 是否可见. 规定时间去找一个元素
# element = driver.find_element(By.ID, "nickname")
locator = (By.NAME,"email")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

# 1. 给元素发送内容
u_element = driver.find_element(By.NAME, "email").send_keys('bella20240229')
driver.find_element(By.CLASS_NAME,"inputNormal").send_keys("admin123!@#")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/form[1]/div[2]/ul/li[4]/span/input").send_keys("15109268472")
time.sleep(5)

# 2. 获取输入内容：是否是自己预期想要输入的
ni_value = driver.find_element(By.NAME, "email").get_attribute("value")
print(ni_value)

# 3. 如何生成用户名 : 随机字符串
for i in range(5):
    # 需要转换一下，直接输出为数组 list
    user_name = ''.join(random.sample("1234567890abcdefg",5))+'@sina.com'
    print(user_name)

# 4. 注册界面，如何拿到验证码 【跳过】
    # 1. 万能验证码  2. 让RD屏蔽该功能  3. 扣 图出来， 通过pytestsseract 库去辨识  (showAPI 第三方收费用  识别不规则验证码)

    
driver.close