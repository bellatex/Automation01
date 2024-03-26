#coding = utf-8
import sys
sys.path.append("D:\\0.automation_testcase\\python_selenium")
from util.excel_util_keyword import ExcelUtil
from keyword_selenium.actionMethod import ActionMethod
import time

class KeywordCase(object):

    def run_main(self): 
        self.action_method = ActionMethod()    
        # 1. excel 中获取 打开浏览器类型
        handle_excel = ExcelUtil("D:\\0.automation_testcase\\python_selenium\\config\\keyword.xls")          
        case_lines = handle_excel.get_lines()
        if case_lines!=None:
            #跳过table header : range(1, rows)
            for i in range(1, case_lines):
                # debug : 写入excel 只有最后一次写入
                # handle_excel.write_value(i, 'pass')
                # continue
                is_run = handle_excel.get_cell_value(i,3)
                if is_run == 'yes':
                    method = handle_excel.get_cell_value(i, 4)
                    send_value = handle_excel.get_cell_value(i, 5)
                    ini_ele_key = handle_excel.get_cell_value(i, 6)
                    except_result_method = handle_excel.get_cell_value(i, 7)
                    except_result = handle_excel.get_cell_value(i, 8)                    
                    #'' 而不是None              
                    self.run_method(method, ini_ele_key, send_value)                    
                    time.sleep(2)
                    if except_result!='':
                        except_value = self.get_except_result_value(except_result)                        
                        if except_value[0] == 'text':
                            actual_reault = self.run_method(except_result_method)
                            print(actual_reault)
                            if except_value[1] in actual_reault:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        if except_value[0] == 'element':
                            actual_reault = self.run_method(except_result_method,except_value[1])
                            time.sleep(10)
                            print(actual_reault)
                            if actual_reault:
                                handle_excel.write_value(i, 'fail')
                            else:
                                handle_excel.write_value(i, 'pass')
                        

    #获取预期结果 
    def get_except_result_value(self, data):
        return data.split('=')    
                     
    #python中不确定参数的函数写法
    def run_method(self,method, ini_ele_key='', send_value='' ):               
        #反射：通过方法名，反射出方法
        method_value = getattr(self.action_method, method) 
        if send_value=='' and ini_ele_key!='':
            result = method_value(ini_ele_key)                                
        elif send_value=='' and ini_ele_key=='':
           result =  method_value()
        else: 
           result =  method_value(ini_ele_key, send_value)   
        return result        
                       

if __name__=='__main__':
    keyword_case = KeywordCase()
    keyword_case.run_main()
        
