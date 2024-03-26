#coding=utf-8
import sys
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest
import HTMLTestRunner
import os
from log.user_log import UserLog



class FirstCase(unittest.TestCase):
    #装饰器
    @classmethod
    def setUpClass(self):
        #调用log module
        self.user_log = UserLog()
        self.logger = self.user_log.get_log()
        #log内容很丰富
        self.logger.debug('This is debug : this open chrome')
        #log内容只有info信息
        # self.logger.info('This is info : this open chrome')
        print("========所有testcase执行前，运行一次=========")

    @classmethod
    def tearDownClass(self):
        
        #关闭释放 log 对象
        self.user_log.close_handle()
        
        print("========所有testcase执行后，运行一次=========")

    #testcase 前置执行
    def setUp(self):        
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.sina.com.cn/register/regmail.php")
        self.driver.maximize_window()
        time.sleep(2)
        self.register_b= RegisterBusiness(self.driver)
        print("************testcase 前置执行")

    #testcase 后置执行
    def tearDown(self):
        time.sleep(2)        
        #判断执行结果，进行错误截图
        # 方式一 ： 自己研究的方式
        if self.tipInfo !='':
            error_pic_path = os.path.join(os.getcwd()+'/report/'+self._testMethodName+'_'+self.tipInfo+'.png')    
            self.driver.save_screenshot(error_pic_path)

        # 方式二： 教学方式， 老报错 未桶
        #if sys.exc_info()[0]   python2 的方法
        # for method_name,error in self._outcome.errors:
        #     case_name = self._testMethodName
        #     error_pic_path = os.path.join(os.getcwd()+'/report/'+case_name+'_'+self.tipInfo+'.png')    
        #     self.driver.save_screenshot(error_pic_path)

        self.driver.close()
        print("************testcase 后置执行")


    # 1. 该邮箱名禁止注册，请换一个再试
    def test_login_email_unableReg_error(self):   
        self.tipInfo = self.register_b.login("d2212", "admin123", "admin123")                
        print("****test_login_email_unableReg_error*****")
        return self.assertNotEqual(len(self.tipInfo), 0, 'Assert_test_login_email_unableReg_error 测试用例执行失败！')
        #通过assert判断是否为error

    # 2. 邮箱名必须是4-16个字符之间（包括4、16）
    def test_login_email_strLong_error(self):
        self.tipInfo = self.register_b.login("d", "admin123", "admin123")        
        print("****test_login_email_strLong_error*****")
        return self.assertNotEqual(len(self.tipInfo), 0, 'Assert_test_login_email_strLong_error 测试用例执行失败！')
        
    # 3. 不能全是数字
    def test_login_email_allNum_error(self):
        self.tipInfo = self.register_b.login("1111", "admin123", "admin123")         
        print("****test_login_email_allNum_error*****")
        return self.assertNotEqual(len(self.tipInfo), 0, 'Assert_test_login_email_allNum_error 测试用例执行失败！')

    # 4. success 用例
    def test_login_email_success(self):
        self.tipInfo = self.register_b.login("test123dd", "admin123", "admin123") 
        print("****test_login_email_success****")
        return self.assertEqual(len(self.tipInfo), 0,  'Assert_test_login_email_success 测试用例执行失败！')

if __name__ == '__main__':
    #1. 跑case方式一 ： 简单的unittest 框架main()函数
    # unittest.main()     
   
    report_path = os.path.join(os.getcwd()+'/report/'+'first_report.html')
    f = open(report_path, 'wb')    
    
    #unittest容器
    suite = unittest.TestSuite()
    #选择只执行其中某几个testcase    
    suite.addTest(FirstCase("test_login_email_unableReg_error"))   
    suite.addTest(FirstCase("test_login_email_strLong_error"))    
    suite.addTest(FirstCase("test_login_email_allNum_error"))    
    suite.addTest(FirstCase("test_login_email_success"))  
    #2. 跑case方式二 ： 使用测试条件
    # unittest.TextTestRunner().run(suite)
    

    # #3. 跑case方式三 ： 生成报告 
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title =' 这个是新浪邮箱注册emil名称测试报告', description = "Bella 第一次 HTMLTestRunner", verbosity =2)
    runner.run(suite)


