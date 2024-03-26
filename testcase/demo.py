#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from business.register_business import RegisterBusiness


if __name__ == '__main__':
    driver =webdriver.Chrome()
    driver.get("https://mail.sina.com.cn/register/regmail.php")
    time.sleep(2)
    register_b = RegisterBusiness(driver)
    # 1. 该邮箱名禁止注册，请换一个再试
    # pw_again_tipInfo = register_b.login("d2212", "admin123", "admin123")

    # 2. 邮箱名必须是4-16个字符之间（包括4、16）
    # pw_again_tipInfo = register_b.login("d", "admin123", "admin123")
    
    # 3. 不能全是数字
    # pw_again_tipInfo = register_b.login("1111", "admin123", "admin123")
    

    # 4. 邮箱名已存在。
    #    可注册test123时通知我
    # pw_again_tipInfo = register_b.login("test123", "admin123", "admin123")   

    # 5. success 用例
    # pw_again_tipInfo = register_b.login("test123dd", "admin123", "admin123")
    
    time.sleep(5)
    driver.close()

