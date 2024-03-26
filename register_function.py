#coding=utf-8
import time
import random
from selenium import webdriver
from base.find_element import FindElement

class RegisterFunction(object):
    # 1. 初始化函数
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    #2. 将driver也写活
    def get_driver(self,url, i):
        if i ==1 :
            driver = webdriver.Chrome()  
        else:
            driver = webdriver.Edge()              
        driver.get(url) 
        driver.maximize_window()
        # time.sleep(3)
        return driver

    #3. 获取元素
    def get_user_element(self,ini_key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(ini_key)
        return user_element

    #4. 随机用户名生成
    def get_range_user(self):
        user_info = ''.join(random.sample("1234567890abcdefg",5))
        return user_info

    #5. 输入用户信息
    def send_user_info(self, ini_key, send_data):
        self.get_user_element(ini_key).send_keys(send_data)

    # 5. driver_exit
    def driver_exit(self):
        print("close driver......")
        self.driver.close()

    # 6. 运行主程序
    def main(self):          
        self.send_user_info("user_email",self.get_range_user())
        self.send_user_info("user_password","admin123")
        self.send_user_info("user_password_again","admin123")
        self.send_user_info("user_phone","15109268472")
        self.send_user_info("user_phonecode","123456")
        register_button = self.get_user_element("user_phonecode")
        print(register_button)
        if register_button == None:
            print("注册成功")
        else:
            print("注册失败 ==>截图错误界面")
            self.driver.save_screenshot("D:\\0.automation_testcase\\python_selenium\\"+self.get_range_user()+".png")
        time.sleep(5)
        
        self.driver_exit()

if __name__ == '__main__':    
    #7. 多浏览器去run testcase
    for i in range(2):      
        register_function = RegisterFunction("https://mail.sina.com.cn/register/regmail.php",i)  
        # register_function.driver_init()
        register_function.main()

    
