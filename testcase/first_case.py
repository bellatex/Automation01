#coding=utf-8
import sys
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from business.register_business import RegisterBusiness
from selenium import webdriver
import time
class FirstCase(object):
    def __init__(self,driver):
        self.register_b= RegisterBusiness(driver)

    def test_login_email_error(self):   
        self.register_b.login("aa","bb","bb") 
        print("****test_login_email*****")
        #通过assert判断是否为error
    
    def test_login_pw_error(self):
        self.register_b.login("aa","bb","bb") 
        print("****test_login_pw*****")

    def test_login_pw_again_error(self):
        self.register_b.login("aa","bb","bb") 
        print("****test_login_pw_again*****")
    
    def test_login_pw_again_info(self):
        print (self.register_b.login("aa11","bb","bb"))

    def test_login_success(self):
        self.register_b.login("aa","bb","bb") 
        print("****test_login_success*****")

def run_main():
    driver =webdriver.Chrome()
    driver.get("https://mail.sina.com.cn/register/regmail.php")
    time.sleep(2)
    login=FirstCase(driver)    
    login.test_login_email_error()
    login.test_login_pw_error()
    login.test_login_pw_again_error()
    login.test_login_success()
    driver.close()

run_main()
