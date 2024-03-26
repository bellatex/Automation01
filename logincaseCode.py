#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


#启动浏览器 实例化
driver = webdriver.Chrome()

# 1. 封装drvier_init
def driver_init(url):
    # 打开url
    # driver.get("https://mail.sina.com.cn/register/regmail.php")    
    driver.get(url)   
    driver.maximize_window()
    time.sleep(3)

# 2. 获取element by name 封装
def get_element(name):
    element = driver.find_element(By.NAME,name)
    return element

# 3. 随机用户名生成
def get_range_user():
    user_info = ''.join(random.sample("1234567890abcdefg",5))+'@sina.com'
    return user_info

# 5. driver_exist
def driver_exist():
    print("close driver......")
    driver.close()

# 6. 运行主程序
def run_main():
    driver_init("https://mail.sina.com.cn/register/regmail.php")
    get_element("email").send_keys(get_range_user())
    time.sleep(5)
    driver_exist()

run_main()
