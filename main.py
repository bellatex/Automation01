import pytest

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest.main(["./pytest.py"])
##################################################################
#  八、持续集成 jenkins
##################################################################
'''
bella ----- admin123


'''
##################################################################
#  七、 日志 log
##################################################################
'''
1. 导入需要的模块
    import logging
    import os
    import datetime
2. 创建loggin.getlogger()对象， --> 定义log等级
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
3. 拼接log_file 路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir,'logs')    
    log_file =  datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
4. 创建文件流对象--> 将logger对象使用文件流对象，将二者结合起来作用
    #2.1 文件流对象 ： 日志输出到文件
    self.file_handle = logging.FileHandler(log_dir+'\\'+log_file, 'a', encoding='utf-8')
    # self.file_handle.setLevel(logging.DEBUG)
    self.file_handle.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s : %(filename)s  %(funcName)s  --> [line]:%(lineno)d :  ---> %(message)s')
    self. file_handle.setFormatter(formatter)
    self.logger.addHandler(self.file_handle)
5. 写入log内容 --> 文件流对象  --> 移除logger对象
    file_handle.close()
    logger.debug('log test formatter')     
    
6. 封装log module后 --> 调用
    #调用log module 放置位置：@classmethod
                             def setUpClass(self):
    logger.debug('This is unittest_case.py : run chrome')
    #关闭释放 防止位置 ：@classmethod
                        def tearDownClass(self): 
    user_log.close_handle()       
'''
##################################################################
#  六、 行为驱动 :  Given  when  and   then 
##################################################################
'''
1. BDD : Behavior driver development 行为驱动开发
   （国内使用比较少）像说话一样写case
2. 使用 
      # Behave（做行为驱动的） 
      # Python 
      # Selenium 
      # Pyhamcrest(做断言)
   2.1 pip install behave
   2.2 pip install byhamcrest


'''
##################################################################
#  五、 设计关键字模型 （没有代码基础）输入->点击->滑动
##################################################################
'''
健壮性，高手写的代码不容易死，异常处理完善
1. excel 梳理 testcase , 分析需要封装的操作
   pip install xlutils
   1.1 二次封装 Excel操作： excel_util_keyword.py
    1.1.1  写入cell 会需要一个模块  ： 
      #获取行数  
      #获取单元格 
      #写入cell  (Fix error ：最终只有最新写入的内容 ： excel_path也必须设定为全局的)    
   1.2 二次封装webdriver : actionMethod.py
      #open_browser
      #get_url
      #get_element
      #send_value
      #click_element
      #sleep_time
      #get_title
      #get_element_text
      #close_browser     
2. 关键字模型
   2.1 读取 excel->testcase->keyword
   2.2 梳理流程->封装 run_method函数
   2.3 判断预期结果+执行结果， excel 中填写执行测试结果pass/fail  

'''

##################################################################
#  四、 数据驱动，及使用 [参数化]
##################################################################
'''
以数据为结果导向
1. 安装数据驱动模块： pip install ddt
    import ddt
    @ddt.data(        
        ["1111", "admin123", "admin123","testcase1","test_login_email_allNum_error"],
        ["d", "admin123", "admin123","testcase2","test_login_email_strLong_error"],
        ["d2212", "admin123", "admin123","testcase3","test_login_email_unableReg_error"],
        ["test123dd", "admin123", "admin123","testcase4","test_login_email_success"]
    )

    @ddt.unpack
    def test_case(self, email, password, password_again,code,error_code):        
        self.tipInfo = self.register_b.login(email, password, password_again)
        self.assertEqual(self.tipInfo,'',code+'测试失败：'+error_code)   
2. 数据通过excel文件 test_data.xls
   Ps. 数据文件必须是.xls ，工具只能识别这个格式
       封装一个ExcelUtil.py 
   2.1 安装数据操作excel模块：pip install xlrd
    from util.excel_util import ExcelUtil
    ex = ExcelUtil()
    data = ex.get_data()
    @ddt.ddt

    @ddt.data(*data) 
    def test_case(self,data):              
        email,password,password_again,code,error_code = data    
        self.tipInfo = self.register_b.login(email, password, password_again)
        self.assertEqual(self.tipInfo,'',code+'测试失败：'+error_code)   

'''
##################################################################
#  三、 uninttest 测试框架 用于单元测试
##################################################################
'''
1. 基本知识
    import unittest
    class TestCase(unittest.TestCase)
    setUp(self)前置处理
    tearDown(self)后置处理，
    每条testcase  命名必须以test开头
    每一条testcase的运行，都会运行一次前置处理+testcase+后置处理
    unittest.main()  执行所有的testcase 
2. 装饰器  @classmethod
    @classmethod
    setUpClass(self)     所有testcase执行前，运行一次
    @classmethod
    tearDownClass(self)  所有testcase执行后，运行一次
3. 测试套件  TestSuit
    unittest容器
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_login_pw_error"))
    unittest.TextTestRunner().run(suite)
4. case执行顺序与跳过 ,也可加跳过执行的条件
   使用装饰器： @unittest.skip("跳过，不执行该条case")
   未修改顺序，是按照字母数字排序依次执行的
5. run_case.py 运行所有case, 程序主入口
   case_path = os.path.join(os.get_cwd(), "testcaseFolder")
   suite = unittest.defaultTestRunnder.discover(case_path, 'unitcase_*.py')
   unittest.TextTestRunner().run(suite)
6. assert 断言的使用
    email_result = self.register_b.login("aa","bb","bb") 
    #assert 判断执行结果, 这里的错误会显示在report.html之中
    self.assertTrue(email_result, 'this is emial_result checked!')    
    self.assertEqual(len(self.tipInfo), 0, 'this is assertEqual Error info : '+self.tipInfo)    
7. 项目中如何生成测试 html report  : import  HTMLTestRunner
8. 运行失败的case截图



'''
##################################################################
#  二、 项目实战PO模型设计与封装 ：抽离+封装+净化,
##################################################################
'''
    页面元素变更，Fix 复用性， 很多不同的页面需要测试
    
    不同页面testcase不同
    精髓 case（封装函数）、数据 、 页面  分开
    1. PO 设计模型Page Object Model页面对象模型：
        1.1 主要体现在对界面交互细节的封装
        1.2 将页面定位和业务操作分开，即 把对象的定位和测试脚本分开，在实际测试中只需要关注 业务流程，从而提高可维护性 
    2. 设计操作层
        page层 (获取页面元素)-->handle层 (操作页面元素）-->business层 --> case层（执行testcase）
'''
##################################################################
#  一、基础部分：浏览器操作 + testcase编写 + 多浏览器执行
##################################################################
'''  
    from selenium import webdriver
    1. 启动浏览器   driver = webdriver.Chrome()
    2. test : 判段打开页面是否正确   EC.title_contains("注册"）
    3. 等待页面load 成功：WebDriverWait  locator = (By.NAME,"email")   WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
    4. 获取元素，给元素发送内容  driver.find_element(By.NAME, "email").send_keys(value)
    5. 获取元素内容（输入内容）：是否是自己预期想要输入的    get_attribute("value")   or driver.find_element(By.NAME, "email").text
    6. 如何生成用户名 : 随机字符串  user_name = ''.join(random.sample("1234567890abcdefg",5))+'@sina.com'

    7. 防止页面元素定位信息变更： 通过配置文件来  localElement.ini --> read_ini.py --> register_function.py
    8. 封装功能 ： def
    9. 把一些代码根据一定格式封装： class 
        封装read_ini.py ==>ReadIni （class）
        封装find_element.py ==>FindElement(class) ： 导入read_ini 模块 中的ReadIni类 实例化类 调用其函数 get_value
        封装register_function.py ==>RegisterFunction(class) : 导入find_element模块 中的FindElement类  实例化类  调用其函数 get_element
    10.封装测试主函数register_function.py
    11.注册失败截图： driver.save_screenshot(image绝对路径)
    12.多浏览器跑testcase: 第一轮：chrome ， 第二轮： ie ， 第三轮： Firefox ，

'''



