import requests 
import pytest
 
# 声明数据 
data = [ 
    {'url': 'https://www.baidu.com', 'expected': '百度一下'}, 
    {'url': 'https://cn.bing.com/', 'expected': 'bing'} 
]
def test_Case1():
    print('this is testcase1')

@pytest.mark.parametrize('case', data)
def test_web(case):    
    url = case['url']    
    expected = case['expected']    
    # 发送API请求，并断言响应的状态码为200，并检查响应文本是否符合预期结果    
    response = requests.get(url)    
    assert response.status_code == 200


 
