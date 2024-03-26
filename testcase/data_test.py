#coding=utf-8
import ddt
import time
from selenium import webdriver
import unittest
import sys
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from business.register_business import RegisterBusiness
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.sina.com.cn/register/regmail.php")
        time.sleep(2)
        self.register_b= RegisterBusiness(self.driver)
        print("******这个是setUp******")

    def tearDown(self):
        self.driver.close()
        print("******这个是tearDown******")

    '''
    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )
    #解包
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)
    '''
    @ddt.data(
        ['1','1','1'],
        ['2','2','2'],
        ['3','3','3']
    )
    @ddt.unpack
    def test_case(self, a, b, c):        
        self.register_b.login(a,b,c)
        


if __name__=='__main__':
    unittest.main()