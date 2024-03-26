#coding=utf-8
import sys
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest

class FirstCase02(unittest.TestCase):
    #装饰器
    @classmethod
    def setUpClass(self):
        print("========所有FirstCase02执行前，运行一次=========")

    @classmethod
    def tearDownClass(self):
        print("========所有FirstCase02执行后，运行一次=========")

    #testcase 前置执行
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.sina.com.cn/register/regmail.php")
        time.sleep(2)
        self.register_b= RegisterBusiness(self.driver)
        print("************testcase 前置执行")

    #testcase 后置执行
    def tearDown(self):
        self.driver.close()
        print("************testcase 后置执行")

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

    def test_login_success(self):
        self.register_b.login("aa","bb","bb") 
        print("****test_login_success*****")

if __name__ == '__main__':
    #unittest容器
    suite = unittest.TestSuite()
    #选择只执行其中某几个testcase
    suite.addTest(FirstCase02("test_login_pw_error"))
    suite.addTest(FirstCase02("test_login_success"))
    unittest.TextTestRunner().run(suite)
