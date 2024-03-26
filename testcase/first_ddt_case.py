#coding=utf-8
import ddt
import time
from selenium import webdriver
import unittest
import sys
import os
import HTMLTestRunner
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.sina.com.cn/register/regmail.php")
        self.driver.maximize_window()
        time.sleep(2)
        self.register_b= RegisterBusiness(self.driver)          
        print("************testcase 前置执行")

    def tearDown(self):
        time.sleep(2)        
        #判断执行结果，进行错误截图
        # 方式一 ： 自己研究的方式
        if self.tipInfo !='':
            error_pic_path = os.path.join(os.getcwd()+'/report/'+self.tipInfo+'.png')    
            self.driver.save_screenshot(error_pic_path)

        # 方式二： 教学方式， 老报错 未通
        #if sys.exc_info()[0]   python2 的方法
        # for method_name,error in self._outcome.errors:
        #     case_name = self._testMethodName
        #     error_pic_path = os.path.join(os.getcwd()+'/report/'+case_name+'_'+self.tipInfo+'.png')    
        #     self.driver.save_screenshot(error_pic_path)

        print("************testcase 后置执行")
        self.driver.close()

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
    # 方法一：
    # @ddt.data(        
    #     ["1111", "admin123", "admin123","testcase1","test_login_email_allNum_error"],
    #     ["d", "admin123", "admin123","testcase2","test_login_email_strLong_error"],
    #     ["d2212", "admin123", "admin123","testcase3","test_login_email_unableReg_error"],
    #     ["test123dd", "admin123", "admin123","testcase4","test_login_email_success"]
    # )

    # @ddt.unpack
    # def test_case(self, email, password, password_again,code,error_code):        
    #     self.tipInfo = self.register_b.login(email, password, password_again)
    #     self.assertEqual(self.tipInfo,'',code+'测试失败：'+error_code)   

    #方法二
    @ddt.data(*data) 
    def test_case(self,data):              
        email,password,password_again,code,error_code = data    
        self.tipInfo = self.register_b.login(email, password, password_again)
        self.assertEqual(self.tipInfo,'',code+'测试失败：'+error_code)   


if __name__=='__main__':
    # unittest.main()
    report_path = os.path.join(os.getcwd()+'/report/'+'first_DDT_report.html')
    f = open(report_path, 'wb') 
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)      
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title =' 这个是DDT参数化测试报告', description = "Bella 第一次 HTMLTestRunner", verbosity =2)
    runner.run(suite)
